import re
from dotenv import dotenv_values

envConfig = dotenv_values(".env")


# Format path for saving file
def path_to_env_var(path: str) -> str:
    # Replace non-alphanumeric characters with underscores
    sanitized = re.sub(r"[^a-zA-Z0-9]", "_", path)

    # Make sure it starts with a letter or underscore
    if not re.match(r"^[a-zA-Z_]", sanitized):
        sanitized = f"_{sanitized}"

    return sanitized.upper()


# Map project_entry_id to project directory
def map_dir_to_proj_id(dir_path, project_entry_ID):
    formatted_dir_path = path_to_env_var(dir_path)
    mapping = f"{formatted_dir_path}={project_entry_ID}\n"
    return mapping


def mapping_exists_in_env(dir_path, proj_id):
    formatted_dir_path = path_to_env_var(dir_path)
    existing_proj_id = envConfig.get(formatted_dir_path, None)
    return existing_proj_id if existing_proj_id == proj_id else False


#  Save dir to proj_id mapping to .env file for future runs
def save_mapping(dir_path, proj_id):
    mapping = map_dir_to_proj_id(dir_path, proj_id)
    print("Saving mapping:", mapping)

    with open(".env", "a") as f:
        f.write(mapping)


def check_for_saved_proj_id(dir_path):
    formatted_dir_path = path_to_env_var(dir_path)
    existing_proj_id = envConfig.get(formatted_dir_path, None)
    return existing_proj_id


def retrieve_proj_id(dir_path, retrying=False):
    formatted_dir_path = path_to_env_var(dir_path)
    saved_proj_id = check_for_saved_proj_id(formatted_dir_path)

    if saved_proj_id and not retrying:
        print("Found project associated with this directory")
        while True:
            answer = input("Use this project entry ID? (Y/n): ")
            if answer == "y" or answer == "":
                return saved_proj_id
            elif answer == "n":
                new_proj_id = input("Enter new project entry ID: ")
                return new_proj_id
            else:
                # Do nothing and prompt user again
                pass
    else:
        new_proj_id = input("Enter project entry ID: ")
        return new_proj_id


def get_project_from_client(client, proj_id):
    try:
        project = client.entry(proj_id)
        return project
    except:
        print("Project not found")
        return False


# Look for project entry ID in .env file
# If it exists, prompt user to use it
# If it doesn't exist, prompt user to enter it
# When project is successfully retrieved, save the project entry ID to .env file and exit loop
def get_project(client, dir_path, proj_id_from_args):
    retrying_proj_id = False
    while True:
        if not retrying_proj_id:
            proj_id = proj_id_from_args or retrieve_proj_id(dir_path)
        else:
            proj_id = retrieve_proj_id(dir_path, retrying=True)
        project = get_project_from_client(client, proj_id)
        if project:
            if not mapping_exists_in_env(dir_path, proj_id):
                save_mapping(dir_path, proj_id)
            return project
        else:
            retrying_proj_id = True
