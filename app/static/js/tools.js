function truncateString(str, num) {
    if (str.length > num) {
        return str.slice(0, num) + "...";
    } else {
        return str;
    }
}

function reject(guid, reason) {
    console.log('reject', reason, guid)
    $.get('/reject/'+guid)
}

function render(block, item) {

    // No Image or Site
    if (!item.image || !item.site) {
        $('[' + block + ']').remove()
        reject(item.guid, 'no-image-site')
        return
    }

    // Remove Top Post From Grid
    if (window.TOP == item.guid) {
        $('[' + block + ']').remove()
        return
    }

    // Check Image 
    var img = $('<img />', {
        src: item.image
    })

    var image = new Image();

    // Image Faild to Load
    img.on('error', function (e) {
        $('[' + block + ']').remove()
        reject(item.guid, 'image-error')
    })

    // Update Post Block
    img.on('load', function() {

        $('[' + block + ']').show()
        $('[' + block + '] [post-title]').html(item.title)
        $('[' + block + '] [post-title]').attr('href', '/read/' + item.guid)
        $('[' + block + '] [post-title]').attr('post-topic', item.topic)
        $('[' + block + '] [post-description]').html(truncateString(item.description, 100))
        $('[' + block + '] [post-site]').html(item.site)

        // Poster Image
        $('[' + block + '] [post-image]').css("background-image", "url(" + item.image + ")");
        if (!$('[' + block + '] [post-image]').attr('style')) {
            reject(item.guid, 'image-error-style')
        }
    });
}