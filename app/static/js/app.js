$(document).ready(function() {

    // $(window.TOPICS).each(function(i, topic) {
    //     loadBlock(topic)
    // })

    var user_data_object = localStorage.getItem('user_data')
    window.user_data = {}

    $(window.TOPICS).each(function(i, topic) {
        user_data[topic] = window.MAX
    });

    // New Users
    if (user_data_object == null) {
        localStorage.setItem('user_data', JSON.stringify(user_data))
    } else {
        window.user_data  = JSON.parse(user_data_object)
    }

    // New Topics
    $(window.TOPICS).each(function(i, topic) {
        if (!window.user_data[topic]) {
            window.user_data[topic] = window.MAX
        }
    });

    // User Data
    if (location.hostname == 'localhost') console.log(window.user_data)


    fetch('/feed',
        {
          method: 'post',
          headers: {
            Accept: 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(window.user_data)
        }
      )
        .then(res => res.json())
        .then(res => {
            $.each(res, function(i, article) {
                render('post-grid'+i, article)
            }) 
        })


    // Open Article
    $(document).on('click', '[post-title]', function(e) {
        var selected_topic = $(this).attr('post-topic')

        $(window.TOPICS).each(function(i, topic) {
            if (selected_topic == topic) {
                window.user_data[topic] += 1
            } else {
                if (user_data[topic] > 6) {
                    window.user_data[topic] -= 1
                }
            }
        });
        localStorage.setItem('user_data', JSON.stringify(user_data))

    })
})
