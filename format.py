from markdown_helpers import links_to_markdown_links, to_markdown_image
from shields import make_shield_str
from contentful_rich_text_to_markdown_converter import convert_rich_text_to_markdown
from content_extractors import extract_img_url_and_title


def format_rich_text(proj, name):
    entity = getattr(proj, name)
    markdown = convert_rich_text_to_markdown(entity)
    return markdown + "\n\n"


def format_img(proj, image_name):
    url_full, title = extract_img_url_and_title(proj, image_name)
    markdown = to_markdown_image(title, url_full)
    return markdown


def format_links(proj):
    links = links_to_markdown_links(proj.links)
    return links


def format_shields(proj):
    acc = ""
    for shield in proj.shields:
        shieldStr = make_shield_str(shield)
        acc += shieldStr + "&nbsp;"
    return acc + "\n\n"
