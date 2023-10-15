import os
import argparse
import sys
from api import connect_to_contentful
from dotenv import dotenv_values
from proj_getter import (
    save_mapping,
    retrieve_proj_id,
    get_project,
    mapping_exists_in_env,
)
from constants import LINE_BREAK
from markdown_helpers import to_markdown_header, to_markdown_header
from constants import SectionType
from format import format_proj_section


# Print warning and prompt user for confirmation
print("WARNING: This script will overwrite any existing README.md and images folder")
while True:
    user_input = input("Continue? (y/n): ")
    if user_input == "y":
        break
    elif user_input == "n":
        sys.exit()
    else:
        # Do nothing and prompt user again
        pass

# Parse arguments
parser = argparse.ArgumentParser()
# Use directory supplied by --cwd argument so that the script can be run from anywhere
parser.add_argument("--cwd", help="Original working directory")
# Use project ID supplied by --proj_id argument if it exists, otherwise prompt user for it
parser.add_argument("--proj_id", help="Project ID")
args = parser.parse_args()

# Check if --cwd argument was supplied. If not: exit
if not args.cwd:
    print("Please supply --cwd argument")
    sys.exit()

# Connect to Contentful API
client = connect_to_contentful()

# Look for project entry ID in .env file
# If it exists, prompt user to use it
# If it doesn't exist, prompt user to enter it
# When project is successfully retrieved, save the project entry ID to .env file and exit loop
retrying_proj_id = False
dir_path = args.cwd
while True:
    if not retrying_proj_id:
        proj_id = args.proj_id or retrieve_proj_id(dir_path)
    else:
        proj_id = retrieve_proj_id(dir_path, retrying=True)
    project = get_project(client, proj_id)
    if project:
        if not mapping_exists_in_env(dir_path, proj_id):
            save_mapping(dir_path, proj_id)
        break
    else:
        retrying_proj_id = True

print("Project requested: ", project.title)

# change working directory to to project folder
os.chdir(args.cwd)

# Defines the order and type of sections to be printed
# Format: (name, type, print_header = False)
section_mappings = [
    ("slogan", SectionType.RICH_TEXT),
    ("header_image", SectionType.IMAGE),
    ("links", SectionType.LINKS),
    ("description", SectionType.RICH_TEXT),
    ("made_with", SectionType.SHIELDS, True),
    ("features", SectionType.RICH_TEXT, True),
    ("preview_gif", SectionType.IMAGE),
    ("usage", SectionType.RICH_TEXT, True),
    ("configure", SectionType.RICH_TEXT, True),
    ("lessons_learned", SectionType.RICH_TEXT, True),
    ("reflection", SectionType.RICH_TEXT, True),
    ("authors", SectionType.RICH_TEXT, True),
    ("acknowledgements", SectionType.RICH_TEXT, True),
    ("custom", SectionType.RICH_TEXT),
]

# Create and add project title separately
project_title = to_markdown_header(project.title, 1)
markdown_sections = [project_title]

# Map through each section and add it's markdown representation to markdown_sections
for section in section_mappings:
    if section == LINE_BREAK:
        markdown_sections.append(LINE_BREAK)
        continue
    name, type, *rest = section
    print_header = rest[0] if rest else False
    markdown = format_proj_section(project, name, type, print_header)
    markdown_sections.append(markdown)

# Join all markdown sections into one string
finalStr = "".join(markdown_sections)
print("Writing to README.md...")
print(finalStr)

# Write contents to README.md
f = open("README.md", "w")
f.write(finalStr)
f.close()
