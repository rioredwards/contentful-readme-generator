import sys
from api import get_project
from markdownHelpers import (
    to_markdown_text,
    slogan_to_markdown_text,
    links_to_markdown_links,
)


# Get project's entry ID from Args. If no Args, exit with error message.
project_entry_ID = (
    sys.argv[1] if len(sys.argv) > 1 else sys.exit("No project entry ID supplied.")
)

# Fetch project entry by ID
project = get_project(project_entry_ID)
print("Project requested: ", project.title)

# Create string for title (Text)
titleStr = to_markdown_text(project.title, "h1")

# ECreate string for slogan (Rich Text)
slogan_rich_text_nodes = project.slogan.get("content")[0].get("content")
slogan_markdown_text = slogan_to_markdown_text(slogan_rich_text_nodes)

# Create string for links (Links)
links = links_to_markdown_links(project.links)

# Write contents to README.md
finalStr = titleStr + slogan_markdown_text + links
print("Writing to README.md...")
print(finalStr)
f = open("README.md", "w")
f.write(finalStr)
f.close()
