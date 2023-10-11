from content_extractors import (
    extract_slogan_text_and_style,
    extract_url_and_display_text,
)


# This function converts any string to formatted markdown
def to_markdown_text(str, style):
    match style:
        case "h1":
            return "# " + str + "\n\n"
        case "h2":
            return "## " + str + "\n\n"
        case "h3":
            return "### " + str + "\n\n"
        case "bold":
            return "**" + str + "**"
        case "italic":
            return "_" + str + "_"
        case _:
            return str


def to_markdown_link(str, url):
    return "[" + str + "](" + url + ")"


def to_markdown_image(str, url):
    return f"![{str}]({url})"


def slogan_to_markdown_text(rich_text):
    accumulator = ""
    for rich_text_obj in rich_text:
        value, type = extract_slogan_text_and_style(rich_text_obj)
        accumulator += to_markdown_text(value, type)
    return accumulator + "\n\n"


def links_to_markdown_links(links):
    accumulator = ""
    for link in links:
        url, text = extract_url_and_display_text(link)
        accumulator += to_markdown_link(text, url) + "&nbsp;"
    return accumulator + "\n\n"
