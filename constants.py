from enum import Enum

LINE_BREAK = "---\n\n"


class SectionType(Enum):
    PLAIN_TEXT = 1
    RICH_TEXT = 2
    IMAGE = 3
    LINKS = 4
    SHIELDS = 5
