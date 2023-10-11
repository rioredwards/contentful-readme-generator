import sys
from api import get_project
from constants import LINE_BREAK
from format import (
    format_title,
    format_slogan,
    format_header,
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
header_str = format_header(project)

# Create string for links (Links)
links_str = format_links(project)

# Create strings for shields (Images)
shields_str = format_shields(project)


# Write contents to README.md
markdown_sections = [
    title_str,
    slogan_str,
    header_str,
    links_str,
    LINE_BREAK,
    shields_str,
]
finalStr = "".join(markdown_sections)
print("Writing to README.md...")
print(finalStr)
f = open("README.md", "w")
f.write(finalStr)
f.close()
