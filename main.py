import sys
from api import get_project
from constants import LINE_BREAK, MADE_WITH_HEADER, FEATURES_HEADER
from markdown_helpers import to_markdown_text
from format import (
    format_title,
    format_rich_text,
    format_header_img,
    format_links,
    format_shields,
    format_rich_text,
)


# Get project's entry ID from Args. If no Args, exit with error message.
project_entry_ID = (
    sys.argv[1] if len(sys.argv) > 1 else sys.exit("No project entry ID supplied.")
)

# Fetch project entry by ID
project = get_project(project_entry_ID)
print("Project requested: ", project.title)

# Create string for title (Text)
title_str = format_title(project)


# Create string for header image (Image)
header_img_str = format_header_img(project)

# Create string for links (Links)
links_str = format_links(project)

# Create string for slogan (Rich Text)
slogan_str = format_rich_text(project, "slogan")

# Create string for description (Rich Text)
description_str = format_rich_text(project, "short_description")

# Create string for features (Rich Text)
features_header = to_markdown_text(FEATURES_HEADER, "h2")
features_str = format_rich_text(project, "features")

# Create strings for shields (Images)
made_with_header = to_markdown_text(MADE_WITH_HEADER, "h2")
shields_str = format_shields(project)


# Create final string for README.md
markdown_sections = [
    title_str,
    slogan_str,
    header_img_str,
    links_str,
    LINE_BREAK,
    description_str,
    made_with_header,
    shields_str,
    features_header,
    features_str,
]
finalStr = "".join(markdown_sections)
print("Writing to README.md...")
print(finalStr)

# Write contents to README.md
f = open("README.md", "w")
f.write(finalStr)
f.close()
