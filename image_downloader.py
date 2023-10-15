import os
import requests
from utils import convert_to_snake_case, get_file_extension_from_url


def generate_file_name_and_extension(title, remote_url):
    new_file_name = convert_to_snake_case(title)
    file_extension = get_file_extension_from_url(remote_url)
    new_file_name_with_extension = f"{new_file_name}.{file_extension}"
    return new_file_name_with_extension


def create_folder(folder_name):
    current_directory = os.getcwd()
    folder_path = os.path.join(current_directory, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def download_image(url, folder_name, file_name):
    current_directory = os.getcwd()
    folder_path = os.path.join(current_directory, folder_name)
    create_folder(folder_name)
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, "wb") as file:
        response = requests.get(url)
        file.write(response.content)
