from content_extractors import extract_shield_info
from markdown_helpers import to_markdown_image

SHIELDS_BASE_URL = "https://img.shields.io/badge/-"


def make_shield_URL(
    shieldTextStr, shieldBGColor, shieldLogoName, shieldLogoColor, shieldStyle
):
    shieldURL = (
        SHIELDS_BASE_URL
        + shieldTextStr
        + "-"
        + shieldBGColor
        + "?logo="
        + shieldLogoName
        + "&logoColor="
        + shieldLogoColor
        + "&style="
        + shieldStyle
    )
    return shieldURL


def make_shield_str(shield_obj):
    info = extract_shield_info(shield_obj)
    URL = make_shield_URL(*info[1:])
    name = info[0]

    shield = to_markdown_image(name, URL)
    return shield
