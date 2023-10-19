import re
import json
from image_downloader import download_image
from markdown_helpers import to_markdown_image


def json_to_markdown(match):
    json_str = match.group(1)
    json_obj = json.loads(json_str)
    title = json_obj["customEmbeddedImage"]["title"]
    remote_url = json_obj["customEmbeddedImage"]["url"]

    local_url = download_image(remote_url, title)

    markdown = to_markdown_image(title, local_url)
    return markdown + "\n\n"


def process_text(text):
    pattern = r'({"customEmbeddedImage":{"title":"[^"]*","url":"[^"]*"}})'
    return re.sub(pattern, json_to_markdown, text)


# Test the function
text1 = 'Some text. {"customEmbeddedImage":{"title":"Test1","url":"URL1"}} More text. {"customEmbeddedImage":{"title":"Test2","url":"URL2"}}'
text2 = '# Test Project\n{"customEmbeddedImage":{"title":"Test Logo","url":"https://images.ctfassets.net/l329ngjcm8m3/61Gv4YS4gh15J9LlabYYGw/c1bb5e48c4fb498e1a83cbcf5ea92085/Test_Logo.png"}}'

after_processing = process_text(text2)

print(f"After processing: {after_processing}")
