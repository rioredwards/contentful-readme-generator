from markdown_helpers import to_markdown_header, to_markdown_image, to_markdown_link
from shields import make_shield_str
from contentful_rich_text_to_markdown_converter import convert_rich_text_to_markdown
from content_extractors import extract_img_url_and_title, extract_url_and_display_text
from constants import SectionType
from image_downloader import download_image
from utils import capitalize_str
from embedded_image_search import download_embedded_images_and_reformat_markdown


def format_rich_text(proj, name):
    markdown_section = getattr(proj, name, None)
    if markdown_section is None:
        return None

    markdown = convert_rich_text_to_markdown(markdown_section)

    # If markdown contains embedded images, download them
    # Then replace stringified JSON with their markdown equivalents and local paths
    markdown_scraped_for_images = download_embedded_images_and_reformat_markdown(
        markdown
    )

    return markdown_scraped_for_images + "\n"


def format_img(proj, image_name):
    proj_fields = proj.fields()
    img_fields = proj_fields[image_name].fields() if image_name in proj_fields else None
    if img_fields is None:
        return None

    contentful_url, title = extract_img_url_and_title(img_fields)

    local_url = download_image(contentful_url, title)

    markdown = to_markdown_image(title, local_url)
    return markdown + "\n\n"


def format_links_section(proj):
    links_section = getattr(proj, "links", None)
    if links_section is None:
        return None

    accumulator = ""
    for i, link in enumerate(links_section):
        url, text = extract_url_and_display_text(link)
        accumulator += to_markdown_link(text, url)
        if i != len(links_section) - 1:
            accumulator += " • "
    return accumulator + "\n\n"


def format_shields(proj):
    shields_section = getattr(proj, "made_with", None)
    if shields_section is None:
        return None

    acc = ""
    for shield in shields_section:
        shieldStr = make_shield_str(shield)
        acc += shieldStr + "&nbsp;"
    return acc + "\n\n"


def format_proj_section(proj, name, type, print_header=False):
    if print_header is not False:
        capitalized_name = capitalize_str(name)
        header = to_markdown_header(capitalized_name, 2)
    else:
        header = ""

    if type == SectionType.IMAGE:
        img_markdown = format_img(proj, name)
        return header + img_markdown if img_markdown else ""
    elif type == SectionType.RICH_TEXT:
        rich_text_markdown = format_rich_text(proj, name)
        return header + rich_text_markdown if rich_text_markdown else ""
    elif type == SectionType.LINKS:
        links_markdown = format_links_section(proj)
        return header + links_markdown if links_markdown else ""
    elif type == SectionType.SHIELDS:
        shields_markdown = format_shields(proj)
        return header + shields_markdown if shields_markdown else ""
    else:
        raise ValueError("Invalid type for format_proj_section")
