from markdown_helpers import to_markdown_header, to_markdown_image, to_markdown_link
from shields import make_shield_str
from contentful_rich_text_to_markdown_converter import convert_rich_text_to_markdown
from content_extractors import extract_img_url_and_title, extract_url_and_display_text
from constants import SectionType
from image_downloader import download_image, generate_file_name_and_extension
from utils import capitalize_str


def format_rich_text(proj, name):
    markdown_section = getattr(proj, name, None)
    if markdown_section is None:
        return ""

    markdown = convert_rich_text_to_markdown(markdown_section)
    return markdown + "\n"


def format_img(proj, image_name):
    proj_fields = proj.fields()
    img_fields = proj_fields[image_name].fields() if image_name in proj_fields else None
    if img_fields is None:
        return ""

    contentful_url, title = extract_img_url_and_title(img_fields)

    folder_name = "images"
    local_file_name = generate_file_name_and_extension(title, contentful_url)
    local_url = f"{folder_name}/{local_file_name}"

    download_image(contentful_url, folder_name, local_file_name)

    markdown = to_markdown_image(title, local_url)
    return markdown + "\n\n"


def format_links_section(proj):
    links_section = getattr(proj, "links", None)
    if links_section is None:
        return ""

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
        return ""

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
        return header + format_img(proj, name)
    elif type == SectionType.RICH_TEXT:
        return header + format_rich_text(proj, name)
    elif type == SectionType.LINKS:
        return header + format_links_section(proj)
    elif type == SectionType.SHIELDS:
        return header + format_shields(proj)
    else:
        raise ValueError("Invalid type for format_proj_section")
