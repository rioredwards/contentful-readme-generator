from content_extractors import (
    extract_url_and_display_text,
)


def to_markdown_header(str, level):
    return "#" * level + " " + str + "\n\n"


def to_markdown_link(str, url):
    return "[" + str + "](" + url + ")"


def to_markdown_image(str, url):
    return f"![{str}]({url})"


def links_to_markdown_links(links):
    accumulator = ""
    for i, link in enumerate(links):
        url, text = extract_url_and_display_text(link)
        accumulator += to_markdown_link(text, url)
        if i != len(links) - 1:
            accumulator += " • "
    return accumulator + "\n\n"
