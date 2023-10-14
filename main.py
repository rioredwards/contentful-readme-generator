import sys
from api import get_project
from constants import LINE_BREAK
from markdown_helpers import to_markdown_header, to_markdown_header
from format import (
    format_rich_text,
    format_img,
    format_links,
    format_shields,
    format_rich_text,
)


# Fetch project entry by ID
project_entry_ID = (
    sys.argv[1] if len(sys.argv) > 1 else sys.exit("No project entry ID supplied.")
)
project = get_project(project_entry_ID)
print("Project requested: ", project.title)

title_str = to_markdown_header(project.title, 1)
header_img_str = format_img(project, "header_image")
preview_gif_str = format_img(project, "preview_gif")
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
lessons_learned_header = to_markdown_header("Lessons Learned", 2)
lessons_learned_str = format_rich_text(project, "lessons_learned")
authors_header = to_markdown_header("Authors", 2)
authors_str = format_rich_text(project, "authors")
acknowledgements_header = to_markdown_header("Acknowledgements", 2)
acknowledgements_str = format_rich_text(project, "acknowledgements")
custom_str = format_rich_text(project, "custom")


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
    lessons_learned_header,
    lessons_learned_str,
    reflection_header,
    reflection_str,
    authors_header,
    authors_str,
    acknowledgements_header,
    acknowledgements_str,
    custom_str,
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
