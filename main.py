import sys
from api import get_project
from constants import LINE_BREAK, TECH_STACK_HEADER
from markdown_helpers import to_markdown_text
from format import (
    format_title,
    format_slogan,
    format_header_img,
    format_links,
    format_shields,
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

# Create string for slogan (Rich Text)
slogan_str = format_slogan(project)

# Create string for header image (Image)
header_str = format_header_img(project)

# Create string for links (Links)
links_str = format_links(project)

# Create strings for shields (Images)
tech_stack_header = to_markdown_text(TECH_STACK_HEADER, "h2")
shields_str = format_shields(project)

# Create final string for README.md
markdown_sections = [
    title_str,
    slogan_str,
    header_str,
    links_str,
    LINE_BREAK,
    tech_stack_header,
    shields_str,
]
finalStr = "".join(markdown_sections)
print("Writing to README.md...")
print(finalStr)

# Write contents to README.md
f = open("README.md", "w")
f.write(finalStr)
f.close()
