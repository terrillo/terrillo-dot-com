import marko


def markdown_parser(markdown):
    HTML = marko.convert(markdown)

    replacements = {
        "[ ]": '<i class="ion-android-radio-button-off"></i>',
        "[x]": '<i class="ion-android-checkmark-circle text-teal-500"></i>',
        "<h1>": '<h1 class="text-3xl font-bold">',
        "</h1>": "</h1>",
        "<h2>": '<h2 class="text-xl font-bold">',
        "</h2>": "</h2>",
        "<h3>": '<p class="h3">',
        "</h3>": "</h3>",
        "<em>": '<em class="text-teal-500">',
    }
    for find in replacements.keys():
        HTML = HTML.replace(find, replacements[find])

    return HTML
