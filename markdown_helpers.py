from content_extractors import (
    extract_text_and_style,
    extract_url_and_display_text,
)


def to_markdown_header(str, level):
    return "#" * level + " " + str + "\n\n"


# This function converts any string to formatted markdown
def to_markdown_text(str, style):
    if style is None:
        return str

    switcher = {
        "bold": f"**{str}**",
        "italic": f"*{str}*",
        "underline": f"<u>{str}</u>",
        "strikethrough": f"~~{str}~~",
        "code": f"`{str}`",
    }
    str = switcher.get(style, str)

    return str


def to_markdown_link(str, url):
    return "[" + str + "](" + url + ")"


def to_markdown_image(str, url):
    return f"![{str}]({url})"


def rich_to_markdown_text(rich_text):
    accumulator = ""
    for rich_text_obj in rich_text:
        value, type = extract_text_and_style(rich_text_obj)
        accumulator += to_markdown_text(value, type)
    return accumulator + "\n\n"


def links_to_markdown_links(links):
    accumulator = ""
    for i, link in enumerate(links):
        url, text = extract_url_and_display_text(link)
        accumulator += to_markdown_link(text, url)
        if i != len(links) - 1:
            accumulator += " • "
    return accumulator + "\n\n"
