import os
import requests
from utils import convert_to_snake_case, get_file_extension_from_url


def generate_local_url(folder_name, local_file_name):
    local_url = f"{folder_name}/{local_file_name}"
    return local_url


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


# This function downloads an image from a remote url and saves it locally, returning the local url
def download_image(remote_url, file_name):
    folder_name = "images"
    local_file_name = generate_file_name_and_extension(file_name, remote_url)
    local_url = generate_local_url(folder_name, local_file_name)

    print(f"Downloading image: {local_url}")

    current_directory = os.getcwd()
    folder_path = os.path.join(current_directory, folder_name)
    create_folder(folder_name)
    file_path = os.path.join(folder_path, local_file_name)
    with open(file_path, "wb") as file:
        response = requests.get(remote_url)
        file.write(response.content)
    return local_url
