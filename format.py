from content_extractors import (
    extract_header_image_url_and_title,
)
from markdown_helpers import (
    links_to_markdown_links,
    to_markdown_image,
)
from shields import make_shield_str
from rich_text import markdown_from_rich_text_objs, extract_rich_text_content


def format_rich_text(proj, name):
    rich_text_objs = extract_rich_text_content(proj, name)
    markdown = markdown_from_rich_text_objs(rich_text_objs)
    return markdown + "\n\n"


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
