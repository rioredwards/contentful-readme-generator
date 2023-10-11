from markdown_helpers import to_markdown_text
from content_extractors import (
    extract_slogan_content,
    extract_header_image_url_and_title,
)
from markdown_helpers import (
    to_markdown_text,
    slogan_to_markdown_text,
    links_to_markdown_links,
    to_markdown_image,
)
from shields import make_shield_str


def format_title(proj):
    return to_markdown_text(proj.title, "h1")


def format_slogan(proj):
    slogan_rich_text_objs = extract_slogan_content(proj)
    return slogan_to_markdown_text(slogan_rich_text_objs)


def format_header_img(proj):
    url, title = extract_header_image_url_and_title(proj)
    return to_markdown_image(url, title)


def format_links(proj):
    links = links_to_markdown_links(proj.links)
    return links


def format_shields(proj):
    acc = ""
    for shield in proj.shields:
        shieldStr = make_shield_str(shield)
        acc += shieldStr + "&nbsp;"
    return acc + "\n\n"
