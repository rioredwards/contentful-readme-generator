from content_extractors import (
    extract_header_image_url_and_title,
    extract_preview_gif_url_and_title,
)
from markdown_helpers import (
    links_to_markdown_links,
    to_markdown_image,
)
from shields import make_shield_str
from contentful_rich_text_to_markdown_converter import convert_rich_text_to_markdown


def format_rich_text(proj, name):
    entity = getattr(proj, name)
    markdown = convert_rich_text_to_markdown(entity)
    return markdown + "\n\n"


def format_header_img(proj):
    url, title = extract_header_image_url_and_title(proj)
    return to_markdown_image(url, title)


def format_preview_gif(proj):
    url, title = extract_preview_gif_url_and_title(proj)
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
