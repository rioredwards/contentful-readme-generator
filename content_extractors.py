def extract_text_and_style(rich_text_objs):
    text = rich_text_objs.get("value")
    marks = rich_text_objs.get("marks")
    if marks is None:
        print(rich_text_objs)
    if len(marks) > 0:
        style = marks[0].get("type")
        return text, style
    else:
        return text, None


def extract_img_url_and_title(proj, image_name):
    fields = proj.fields()[image_name].fields()
    title = fields.get("title")
    url_endpoint = fields.get("file").get("url")
    url_full = "https:" + url_endpoint
    return url_full, title


def extract_description_text_and_style(slogan_objs):
    text = slogan_objs.get("value")
    marks = slogan_objs.get("marks")
    if len(marks) > 0:
        style = marks[0].get("type")
        return text, style
    else:
        return text, None


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
