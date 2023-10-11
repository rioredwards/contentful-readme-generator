def extract_slogan_content(proj):
    return proj.slogan.get("content")[0].get("content")


def extract_description_content(proj):
    return proj.short_description.get("content")[0].get("content")


def extract_text_and_style(rich_text_objs):
    text = rich_text_objs.get("value")
    marks = rich_text_objs.get("marks")
    if len(marks) > 0:
        style = marks[0].get("type")
        return text, style
    else:
        return text, None


def extract_description_text_and_style(slogan_objs):
    text = slogan_objs.get("value")
    marks = slogan_objs.get("marks")
    if len(marks) > 0:
        style = marks[0].get("type")
        return text, style
    else:
        return text, None


def extract_header_image_url_and_title(proj):
    title = proj.fields()["header_image"].fields().get("title")
    url_endpoint = proj.fields()["header_image"].fields().get("file").get("url")
    url_full = "https:" + url_endpoint
    return title, url_full


def extract_url_and_display_text(link):
    url = link.url
    displayText = link.fields()["display_text"]
    return url, displayText


def extract_shield_info(shield):
    name = shield.fields()["name"]
    textStr = shield.fields()["text"]
    bgColor = shield.fields()["background_color"]
    logoName = shield.fields()["logo_name"]
    logoColor = shield.fields()["logo_color"]
    style = shield.fields()["style"]
    return name, textStr, bgColor, logoName, logoColor, style
