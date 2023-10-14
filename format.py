from markdown_helpers import to_markdown_header, to_markdown_image, to_markdown_link
from shields import make_shield_str
from contentful_rich_text_to_markdown_converter import convert_rich_text_to_markdown
from content_extractors import extract_img_url_and_title, extract_url_and_display_text
from constants import SectionType


def format_rich_text(proj, name):
    entity = getattr(proj, name)
    markdown = convert_rich_text_to_markdown(entity)
    return markdown + "\n"


def format_img(proj, image_name):
    url_full, title = extract_img_url_and_title(proj, image_name)
    markdown = to_markdown_image(title, url_full)
    return markdown + "\n\n"


def format_links_section(proj):
    links = proj.links
    accumulator = ""
    for i, link in enumerate(links):
        url, text = extract_url_and_display_text(link)
        accumulator += to_markdown_link(text, url)
        if i != len(links) - 1:
            accumulator += " • "
    return accumulator + "\n\n"


def format_shields(proj):
    acc = ""
    for shield in proj.made_with:
        shieldStr = make_shield_str(shield)
        acc += shieldStr + "&nbsp;"
    return acc + "\n\n"


def format_proj_section(proj, name, type, print_header=False):
    if print_header is not False:
        capitalized_name = name.replace("_", " ").capitalize()
        header = to_markdown_header(capitalized_name, 2)
    else:
        header = ""

    if type == SectionType.RICH_TEXT:
        return header + format_rich_text(proj, name)
    elif type == SectionType.IMAGE:
        return header + format_img(proj, name)
    elif type == SectionType.LINKS:
        return header + format_links_section(proj)
    elif type == SectionType.SHIELDS:
        return header + format_shields(proj)
    else:
        raise ValueError("Invalid type for format_proj_section")
