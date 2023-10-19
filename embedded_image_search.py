import re
import json


def json_to_markdown(match):
    json_str = match.group(1)
    json_obj = json.loads(json_str)
    title = json_obj["customEmbeddedImage"]["title"]
    url = json_obj["customEmbeddedImage"]["url"]
    return f"![{title}]({url})"


def process_text(text):
    pattern = r'({"customEmbeddedImage":{"title":"[^"]*","url":"[^"]*"}})'
    return re.sub(pattern, json_to_markdown, text)


# Test the function
text = 'Some text. {"customEmbeddedImage":{"title":"Test1","url":"URL1"}} More text. {"customEmbeddedImage":{"title":"Test2","url":"URL2"}}'
after_processing = process_text(text)

print(f"After processing: {after_processing}")
