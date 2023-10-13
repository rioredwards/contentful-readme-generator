import sys
from api import get_project
from constants import LINE_BREAK
from markdown_helpers import to_markdown_header, to_markdown_header
from format import (
    format_rich_text,
    format_header_img,
    format_preview_gif,
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

title_str = to_markdown_header(project.title, 1)
header_img_str = format_header_img(project)
preview_gif_str = format_preview_gif(project)
links_str = format_links(project)
made_with_header = to_markdown_header("Made With", 2)
shields_str = format_shields(project)
usage_header = to_markdown_header("Usage", 2)
usage_str = format_rich_text(project, "usage")
slogan_str = format_rich_text(project, "slogan")
description_str = format_rich_text(project, "short_description")
features_header = to_markdown_header("Features", 2)
features_str = format_rich_text(project, "features")
configure_header = to_markdown_header("Configure", 2)
configure_str = format_rich_text(project, "configure")
reflection_header = to_markdown_header("Reflection", 2)
reflection_str = format_rich_text(project, "reflection")

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
    preview_gif_str,
    usage_header,
    usage_str,
    configure_header,
    configure_str,
    reflection_header,
    reflection_str,
]

for section in markdown_sections:
    print(section)

finalStr = "".join(markdown_sections)
print("Writing to README.md...")
print(finalStr)

# Write contents to README.md
f = open("README.md", "w")
f.write(finalStr)
f.close()
