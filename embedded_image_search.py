import re
import json
from image_downloader import download_image
from markdown_helpers import to_markdown_image


def parse_and_download_embedded_img(match):
    json_str = match.group(1)
    json_obj = json.loads(json_str)
    title = json_obj["customEmbeddedImage"]["title"]
    remote_url = json_obj["customEmbeddedImage"]["url"]

    local_url = download_image(remote_url, title)

    markdown = to_markdown_image(title, local_url)
    return markdown


def download_embedded_images_and_reformat_markdown(text):
    pattern = r'({"customEmbeddedImage":{"title":"[^"]*","url":"[^"]*"}})'
    return re.sub(pattern, parse_and_download_embedded_img, text)
