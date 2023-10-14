def to_markdown_header(str, level):
    return "#" * level + " " + str + "\n\n"


def to_markdown_link(str, url):
    return "[" + str + "](" + url + ")"


def to_markdown_image(name, url):
    return f"![{name}]({url})"
