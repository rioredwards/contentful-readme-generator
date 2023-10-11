import sys
from api import get_project, retrieve_image
from markdownHelpers import (
    to_markdown_text,
    slogan_to_markdown_text,
    links_to_markdown_links,
    to_markdown_image,
)
from constants import LINE_BREAK
from shields import make_shield_str


# Get project's entry ID from Args. If no Args, exit with error message.
project_entry_ID = (
    sys.argv[1] if len(sys.argv) > 1 else sys.exit("No project entry ID supplied.")
)

# Fetch project entry by ID
project = get_project(project_entry_ID)
print("Project requested: ", project.title)

# Create string for title (Text)
titleStr = to_markdown_text(project.title, "h1")

# Create string for slogan (Rich Text)
slogan_rich_text_nodes = project.slogan.get("content")[0].get("content")
slogan_text = slogan_to_markdown_text(slogan_rich_text_nodes)

# Create string for header image (Image)
header_image_url_endpoint = (
    project.fields()["header_image"].fields().get("file").get("url")
)
header_image_url_full = "https://" + header_image_url_endpoint
header_image_title = project.fields()["header_image"].fields().get("title")
header_image = to_markdown_image(header_image_title, header_image_url_full)

# Create string for links (Links)
links = links_to_markdown_links(project.links)

# Create strings for shields (Images)
shield = project.shields[0]
shieldStr = make_shield_str(shield)


# Write contents to README.md
markdown_sections = [titleStr, slogan_text, header_image, links, LINE_BREAK, shieldStr]
finalStr = "".join(markdown_sections)
# print("Writing to README.md...")
# print(finalStr)
f = open("README.md", "w")
f.write(finalStr)
f.close()
