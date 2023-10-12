# This function converts any string to formatted markdown
def to_markdown_text(str, style):
    if style is None:
        return str

    switcher = {
        "bold": f"**{str}**",
        "italic": f"*{str}*",
        "underline": f"<u>{str}</u>",
        "strikethrough": f"~~{str}~~",
        "code": f"`{str}`",
    }
    str = switcher.get(style, str)

    return str


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


# Should return a list where each element describes an element in the rich text
# Each element in the list should be either:
# a text text obj: {"type": "text", "text": "Some text", "styles": []},
# a link obj: {"type": "hyperlink", "text": "Display Text", "styles": [], "url": "https://www.google.com"}
# or another list of objects if it's an ordered list
# e.g.
[
    {"type": "text", "text": "\n", "styles": []},
    {
        "type": "ordered-list",
        "children": [
            {"type": "text", "text": "Pull the lever to start.", "styles": []},
            {"type": "text", "text": "\n", "styles": []},
            {
                "type": "ordered-list",
                "children": [
                    {"type": "text", "text": "Eat some rice", "styles": []},
                    {"type": "text", "text": "Eat some beans", "styles": []},
                ],
                "styles": [],
            },
            {"type": "text", "text": "\n", "styles": []},
            {
                "type": "text",
                "text": "Click on the stop buttons to stop the reels.",
                "styles": [],
            },
            {
                "type": "text",
                "text": "Once all the reels have stopped, your quest will be printed out on the display panel.",
                "styles": [],
            },
            {"type": "text", "text": "Get coding!", "styles": []},
        ],
        "styles": [],
    },
    {"type": "text", "text": "\n", "styles": []},
]


def extract_values_and_styles(
    data, inside_ordered_list=False, accumulator=None, inside_hyperlink=False
):
    if accumulator is None:
        accumulator = []

    if isinstance(data, dict):
        node_type = data.get("nodeType")
        is_ordered_list = node_type == "ordered-list"

        local_accumulator = []

        if node_type == "hyperlink":
            process_hyperlink(data, inside_ordered_list, accumulator)
            inside_hyperlink = True

        elif node_type == "text" and not inside_hyperlink:
            process_text(data, inside_ordered_list, accumulator)

        for _, val in data.items():
            if val is None or len(val) == 0:
                continue

            extract_values_and_styles(
                val,
                inside_ordered_list=is_ordered_list or inside_ordered_list,
                accumulator=local_accumulator if is_ordered_list else accumulator,
                inside_hyperlink=inside_hyperlink,
            )

        if is_ordered_list:
            # Add newline object before and after ordered-list
            # accumulator.append({"type": "text", "text": "\n", "styles": []})
            accumulator.append(
                {
                    "type": "ordered-list",
                    "children": local_accumulator,
                    "styles": [],
                }
            )
            # accumulator.append({"type": "text", "text": "\n", "styles": []})

    elif isinstance(data, list):
        for item in data:
            extract_values_and_styles(
                item,
                inside_ordered_list,
                accumulator,
                inside_hyperlink,
            )

    return accumulator if not inside_ordered_list else []


def extract_rich_text_content(proj, name):
    entity = getattr(proj, name)
    simplified_rich_text_data = extract_values_and_styles(entity)
    print(simplified_rich_text_data)
    return simplified_rich_text_data


def markdown_from_rich_text_objs(data, is_ordered_list=False, nest_level=0):
    result = ""
    for idx, item in enumerate(data):
        if isinstance(item, dict):
            item_type = item.get("type")
            text = item.get("text")
            styles = item.get("styles", [])
            url = item.get("url", None)

            if item_type == "ordered-list":
                # Handle nested lists by recursively calling the function on its children
                is_first_ordered_list = not is_ordered_list
                new_nest_level = 0 if is_first_ordered_list else nest_level + 1
                result += markdown_from_rich_text_objs(
                    item["children"], is_ordered_list=True, nest_level=new_nest_level
                )
                continue

            # Apply styles if any
            for style in styles:
                text = to_markdown_text(text, style)

            # Handle hyperlink separately
            if item_type == "hyperlink":
                text = f"[{text}]({url})"

            # Ordered list numbering and indentation
            if is_ordered_list:
                indent = "   " * nest_level
                if nest_level % 2 == 1:
                    # If nest_level is odd, use letters instead of numbers
                    letter = chr(ord("A") + idx)
                    result += f"{indent}{letter}. {text}\n\n"
                else:
                    result += f"{indent}{idx + 1}. {text}\n\n"
            else:
                result += f"{text}"

        elif isinstance(item, list):
            # Recursively handle nested lists
            result += markdown_from_rich_text_objs(
                item, is_ordered_list=True, nest_level=nest_level + 1
            )

    return result
