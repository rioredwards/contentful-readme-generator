# This function converts any string to formatted markdown
def to_markdown_text(str, style):
    match style:
        case "h1":
            return "# " + str + "\n\n"
        case "h2":
            return "## " + str + "\n\n"
        case "h3":
            return "### " + str + "\n\n"
        case "bold":
            return "**" + str + "**"
        case "italic":
            return "_" + str + "_"
        case _:
            return str


def rich_text_to_markdown_text(rich_text):
    accumulator = ""
    for obj in rich_text:
        value = obj.get("value")
        marks = obj.get("marks")
        type = marks[0].get("type") if len(marks) > 0 else None
        accumulator += to_markdown_text(value, type)
    return accumulator
