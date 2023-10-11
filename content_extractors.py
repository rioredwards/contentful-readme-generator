def extract_values_and_marks(data, inside_ordered_list=False, accumulator=None):
    if accumulator is None:
        accumulator = []

    result = []

    if isinstance(data, dict):
        node_type = data.get("nodeType")
        is_ordered_list = node_type == "ordered-list"
        value = data.get("value", None)
        marks = data.get("marks", None)

        if node_type == "text":
            item = (value, marks)
            if inside_ordered_list:
                accumulator.append(item)
            else:
                result.append(item)

        for _, val in data.items():
            if val is None or len(val) == 0:
                continue
            nested_result = extract_values_and_marks(
                val,
                inside_ordered_list=is_ordered_list or inside_ordered_list,
                accumulator=accumulator
                if (is_ordered_list or inside_ordered_list)
                else None,
            )
            if nested_result:
                result.extend(nested_result)

        if is_ordered_list and accumulator:
            result.append(accumulator.copy())
            accumulator.clear()

    elif isinstance(data, list):
        for item in data:
            nested_result = extract_values_and_marks(
                item, inside_ordered_list, accumulator if inside_ordered_list else None
            )
            if nested_result:
                result.extend(nested_result)

    return result


# Should return a list
# Each element is either a tuple (text, style) or another list
def extract_rich_text_content(proj, name):
    entity = getattr(proj, name)
    text = extract_values_and_marks(entity)
    print(text)
    # formatted_list = []
    # content = entity.get("content")
    # contentLength = len(content)
    # if contentLength == 0:
    #     print("No content found for " + name)
    #     return None
    # for obj in content:
    #     type = obj.get("nodeType")
    #     if type == "text":
    #         formatted_list.append(obj)
    #     else:
    #         print("Unrecognized type: " + type)


def extract_rich_text_content_from_obj(obj):
    return obj.get("content")[0].get("content")


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
