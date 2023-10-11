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
    name = shield_obj.fields()["name"]
    textStr = shield_obj.fields()["text"]
    bgColor = shield_obj.fields()["background_color"]
    logoName = shield_obj.fields()["logo_name"]
    logoColor = shield_obj.fields()["logo_color"]
    style = shield_obj.fields()["style"]

    shield_URL = make_shield_URL(textStr, bgColor, logoName, logoColor, style)

    shield = f"![{name}]({shield_URL})"
    return shield
