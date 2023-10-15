import requests
from utils import convert_to_snake_case, get_file_extension_from_url


def generate_file_name_and_extension(title, remote_url):
    new_file_name = convert_to_snake_case(title)
    file_extension = get_file_extension_from_url(remote_url)
    new_file_name_with_extension = f"{new_file_name}.{file_extension}"
    return new_file_name_with_extension


def download_image(url, file_name):
    with open(file_name, "wb") as file:
        response = requests.get(url)
        file.write(response.content)
