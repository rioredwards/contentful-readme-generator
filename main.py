import sys
from api import get_project
from constants import LINE_BREAK
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

# Create strings for shields (Images)
made_with_header = to_markdown_text("Made With", "h2")
shields_str = format_shields(project)

# Create string for slogan (Rich Text)
slogan_str = format_rich_text(project, "slogan")

# Create string for description (Rich Text)
description_str = format_rich_text(project, "short_description")

# Create string for features (Rich Text)
features_header = to_markdown_text("Features", "h2")
features_str = format_rich_text(project, "features")

# Create string for usage (Rich Text)
usage_header = to_markdown_text("Usage", "h2")
usage_str = format_rich_text(project, "usage")
print(usage_str)

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
    usage_header,
    usage_str,
]
finalStr = "".join(markdown_sections)
print("Writing to README.md...")
print(finalStr)

# Write contents to README.md
f = open("README.md", "w")
f.write(finalStr)
f.close()

# proj=  {'title': 'Code Quest', 'slug': 'code-quest', 'slogan': {'data': {}, 'content': [{'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'Level-Up your code with ', 'nodeType': 'text'}, {'data': {}, 'marks': [{'type': 'bold'}], 'value': 'Code Quest', 'nodeType': 'text'}, {'data': {}, 'marks': [], 'value': '!', 'nodeType': 'text'}], 'nodeType': 'paragraph'}], 'nodeType': 'document'}, 'header_image': <Asset id='4QkRN0AaZHDZgk5I9DHTPc' url='//images.ctfassets.net/l329ngjcm8m3/4QkRN0AaZHDZgk5I9DHTPc/74c033b40d980b8cbba803a174e1eb81/banner.png'>, 'links': [<Entry[link] id='7C8x4XsC4EbSMFiEOsRTtG'>, <Entry[link] id='RL2Qeh4Zx0dodzCUg4JNv'>], 'short_description': {'data': {}, 'content': [{'data': {}, 'content': [{'data': {}, 'marks': [], 'value': 'This immersive web app generates pseudo-random coding challenges, making learning practical coding skills ', 'nodeType': 'text'}, {'data': {}, 'marks': [{'type': 'bold'}], 'value': 'exciting', 'nodeType': 'text'}, {'data': {}, 'marks': [], 'value': ' and ', 'nodeType': 'text'}, {'data': {}, 'marks': [{'type': 'bold'}], 'value': 'engaging', 'nodeType': 'text'}, {'data': {}, 'marks': [], 'value': '!', 'nodeType': 'text'}], 'nodeType': 'paragraph'}], 'nodeType': 'document'}, 'shields': [<Entry[shield] id='5vPZxSzaj9PYNC3os5B4A'>, <Entry[shield] id='3adck4RDr7M70ExRqcA9hq'>], 'features': {'nodeType': 'document', 'data': {}, 'content': [{'nodeType': 'paragraph', 'data': {}, 'content': [{'nodeType': 'text', 'value': '- ', 'marks': [], 'data': {}}, {'nodeType': 'text', 'value': 'Choose Your Own Adventure', 'marks': [{'type': 'bold'}], 'data': {}}, {'nodeType': 'text', 'value': ': Users can have quests generated completely at random, or they may specify certain parameters, such as the time limit, and the programming language.\n- ', 'marks': [], 'data': {}}, {'nodeType': 'text', 'value': 'Realistic Challenges', 'marks': [{'type': 'bold'}], 'data': {}}, {'nodeType': 'text', 'value': ": Code Quest will never create a quest that doesn't make sense (eg: CLI quest using React). A sophisticated algorithm ensures that any quest generated is feasible.\n- ", 'marks': [], 'data': {}}, {'nodeType': 'text', 'value': 'Intuitive UI', 'marks': [{'type': 'bold'}], 'data': {}}, {'nodeType': 'text', 'value': ': The UI was designed to resemble a slot machine, giving the app a familiar feel and making it easy to get started. If you do get stuck, there is a built-in help menu to explain the various features.\n- ', 'marks': [], 'data': {}}, {'nodeType': 'text', 'value': 'Smooth Animations', 'marks': [{'type': 'bold'}], 'data': {}}, {'nodeType': 'text', 'value': ': This app makes heavy use of the Framer Motion animation library, which brings the UI to life!\n- C', 'marks': [], 'data': {}}, {'nodeType': 'text', 'value': 'ustom Artwork', 'marks': [{'type': 'bold'}], 'data': {}}, {'nodeType': 'text', 'value': ': All artwork is custom-made, giving Code Quest a unique look and feel.\n- ', 'marks': [], 'data': {}}, {'nodeType': 'text', 'value': 'Well Vetted', 'marks': [{'type': 'bold'}], 'data': {}}, {'nodeType': 'text', 'value': ': The creator of this app, Rio Edwards, has completed nearly 100 coding challenges and projects similar to the ones generated by Code Quest. You can trust these challenges are practical and relevant to real-world coding scenarios.', 'marks': [], 'data': {}}]}]}, 'preview_gif': <Asset id='3LXNCgaTgVhIL2k4SkAWLP' url='//images.ctfassets.net/l329ngjcm8m3/3LXNCgaTgVhIL2k4SkAWLP/1e38876f67eb55d31ad6962f883323e9/Code-Quest-Preview-Gif-_Optimized_.gif'>, 'tags': [<Entry[tag] id='5h9VHMDlliq36vWUHKdmWW'>, <Entry[tag] id='6fvaujQfUrWHrz0Yla4Lnv'>], 'logo': <Asset id='8kxljZRiaZmwQ5oolCwSe' url='//images.ctfassets.net/l329ngjcm8m3/8kxljZRiaZmwQ5oolCwSe/20cb589bd2a045a493ff9f7b448c3cd1/logo512.png'>}
