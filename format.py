from markdown_helpers import to_markdown_text
from content_extractors import (
    extract_rich_text_content,
    extract_header_image_url_and_title,
    extract_rich_text_content_from_obj,
)
from markdown_helpers import (
    to_markdown_text,
    rich_to_markdown_text,
    links_to_markdown_links,
    to_markdown_image,
)
from shields import make_shield_str


def format_title(proj):
    return to_markdown_text(proj.title, "h1")


def format_rich_text(proj, name):
    rich_text_objs = extract_rich_text_content(proj, name)
    print(rich_text_objs)
    # sample_obj = rich_text_objs[0]
    # type = sample_obj.get("nodeType")
    # if type == "text":
    #     return rich_to_markdown_text(rich_text_objs)
    # elif type == "list-item":
    #     accumulator = ""
    #     for i, obj in enumerate(rich_text_objs):
    #         extracted_obj = extract_rich_text_content_from_obj(obj)
    #         list_number = i + 1
    #         accumulator += f"{list_number}. " + rich_to_markdown_text(extracted_obj)
    #     return accumulator
    # else:
    #     print("Unrecognized type: " + type)


# result = [
#     [
#         ("Pull the lever to start.", []),
#         ("Click on the stop buttons to stop the reels.", []),
#         (
#             "Once all the reels have stopped, your quest will be printed out on the display panel.",
#             [],
#         ),
#         ("Get coding!", []),
#     ]
# ]

result = [
    [],
    [("Pull the lever to start.", [])],
    [("Click on the stop buttons to stop the reels.", [])],
    [
        (
            "Once all the reels have stopped, your quest will be printed out on the display panel.",
            [],
        )
    ],
    [("Get coding!", [])],
    ("", []),
]


def format_header_img(proj):
    url, title = extract_header_image_url_and_title(proj)
    return to_markdown_image(url, title)


def format_links(proj):
    links = links_to_markdown_links(proj.links)
    return links


def format_shields(proj):
    acc = ""
    for shield in proj.shields:
        shieldStr = make_shield_str(shield)
        acc += shieldStr + "&nbsp;"
    return acc + "\n\n"
