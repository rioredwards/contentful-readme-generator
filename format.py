from markdown_helpers import to_markdown_text
from content_extractors import (
    extract_rich_text_content,
    extract_header_image_url_and_title,
    extract_rich_text_content_from_obj,
)
from markdown_helpers import (
    to_markdown_text,
    rich_to_markdown_text,
    links_to_markdown_links,
    to_markdown_image,
)
from shields import make_shield_str


def markdown_from_rich_text_objs(data, is_ordered_list=False):
    result = ""

    for idx, item in enumerate(data):
        if isinstance(item, tuple):
            text, styles = item
            if styles is not None:
                for style in styles:
                    text = to_markdown_text(text, style)

            if is_ordered_list:
                result += f"{idx + 1}. {text}\n"
            else:
                result += f"{text}"

        elif isinstance(item, list):
            # Recursively handle nested lists
            result += markdown_from_rich_text_objs(item, is_ordered_list=True)

    return result


def format_rich_text(proj, name):
    rich_text_objs = extract_rich_text_content(proj, name)
    accumulator = markdown_from_rich_text_objs(rich_text_objs)
    return accumulator + "\n\n"


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
