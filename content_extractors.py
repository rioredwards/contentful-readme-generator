# Should return a list where each element describes an element in the rich text
# Each element in the list should be either:
# a text text obj: {"type": "text", "text": "Some text", "styles": []},
# a link obj: {"type": "hyperlink", "text": "Display Text", "styles": [], "url": "https://www.google.com"}
# or another list of objects if it's an ordered list
# e.g.
[
    {"type": "text", "text": "Some text", "styles": []},
    {"type": "text", "text": "Some bold text", "styles": ["bold"]},
    {"type": "text", "text": "Some bold, italic text", "styles": ["bold", "italic"]},
    {
        "type": "hyperlink",
        "text": "Google",
        "styles": [],
        "url": "https://www.google.com",
    },
    {
        "type": "hyperlink",
        "text": "Some bold link",
        "styles": ["bold"],
        "url": "https://www.google.com",
    },
    [
        {"type": "text", "text": "First item in an ordered list", "styles": []},
        {"type": "text", "text": "Second item in an ordered list", "styles": ["bold"]},
    ],
]


def process_hyperlink(node, inside_ordered_list, accumulator):
    item = {
        "type": "hyperlink",
        "text": node.get("content")[0].get("value"),
        "styles": [],
        "url": node.get("data").get("uri"),
    }
    if inside_ordered_list:
        accumulator.append(item)
    else:
        return [item]
    return []


def process_text(node, inside_ordered_list, accumulator):
    value = node.get("value", None)
    marks = node.get("marks", [])
    styles = [mark.get("type") for mark in marks] if marks else []

    if not value.strip() and not styles:
        return []

    item = {"type": "text", "text": value, "styles": styles}
    if inside_ordered_list:
        accumulator.append(item)
    else:
        return [item]
    return []


def extract_values_and_styles(
    data, inside_ordered_list=False, accumulator=None, inside_hyperlink=False
):
    if accumulator is None:
        accumulator = []

    result = []

    if isinstance(data, dict):
        node_type = data.get("nodeType")
        is_ordered_list = node_type == "ordered-list"

        if node_type == "hyperlink":
            result.extend(process_hyperlink(data, inside_ordered_list, accumulator))
            inside_hyperlink = True

        elif node_type == "text" and not inside_hyperlink:
            result.extend(process_text(data, inside_ordered_list, accumulator))

        for _, val in data.items():
            if val is None or len(val) == 0:
                continue

            nested_result = extract_values_and_styles(
                val,
                inside_ordered_list=is_ordered_list or inside_ordered_list,
                accumulator=accumulator
                if is_ordered_list or inside_ordered_list
                else None,
                inside_hyperlink=inside_hyperlink,
            )
            result.extend(nested_result)

        if is_ordered_list and accumulator:
            # Add newline object before ordered-list
            result.append({"type": "text", "text": "\n", "styles": []})
            result.append(accumulator.copy())
            # Add newline object after ordered-list
            result.append({"type": "text", "text": "\n", "styles": []})
            accumulator.clear()

    elif isinstance(data, list):
        for item in data:
            nested_result = extract_values_and_styles(
                item,
                inside_ordered_list,
                accumulator if inside_ordered_list else None,
                inside_hyperlink,
            )
            result.extend(nested_result)

    return result


def extract_rich_text_content(proj, name):
    entity = getattr(proj, name)
    simplified_rich_text_data = extract_values_and_styles(entity)
    return simplified_rich_text_data


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


reflection_data_model = {
    "en-US": {
        "nodeType": "document",
        "data": {},
        "content": [
            {
                "nodeType": "paragraph",
                "data": {},
                "content": [
                    {"nodeType": "text", "value": "", "marks": [], "data": {}},
                    {
                        "nodeType": "hyperlink",
                        "data": {
                            "uri": "https://github.com/rioredwards/code-quest/edit/main/README.md"
                        },
                        "content": [
                            {
                                "nodeType": "text",
                                "value": "GitHub",
                                "marks": [],
                                "data": {},
                            }
                        ],
                    },
                    {"nodeType": "text", "value": "", "marks": [], "data": {}},
                ],
            }
        ],
    }
}
