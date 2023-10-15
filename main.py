import os
import argparse
import sys
from api import get_project
from constants import LINE_BREAK
from markdown_helpers import to_markdown_header, to_markdown_header
from constants import SectionType
from format import format_proj_section

# Print warning and prompt user for confirmation
print("WARNING: This script will overwrite any existing README.md and images/ folder")
print("Press enter to continue or esc to exit")

# Wait for user input
while True:
    user_input = input()
    if user_input == "":
        break
    elif user_input == "\x1b":
        print("Exiting script...")
        sys.exit()

# Parse arguments
parser = argparse.ArgumentParser()
# Use directory supplied by --cwd argument so that the script can be run from anywhere
parser.add_argument("--cwd", help="Original working directory")
# Use project ID supplied by --proj_id argument if it exists, otherwise prompt user for it
parser.add_argument("--proj_id", help="Project ID")
args = parser.parse_args()

# If --cwd argument exists, change working directory to it
# Otherwise, exit the script
if args.cwd:
    os.chdir(args.cwd)
else:
    print("Please supply --cwd argument")
    sys.exit()

# Fetch project entry by ID
project_entry_ID = args.proj_id if args.proj_id else input("Enter project entry ID: ")
try:
    project = get_project(project_entry_ID)
except:
    print("Project not found")
    sys.exit()

print("Project requested: ", project.title)

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
