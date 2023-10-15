def capitalize_str(name):
    return name.replace("_", " ").capitalize()


def convert_to_snake_case(name):
    return name.replace(" ", "_").lower()


def get_file_extension_from_url(url):
    return url.split(".")[-1]
