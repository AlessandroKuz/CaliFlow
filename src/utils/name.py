import json


def get_name(file_path: str) -> str | None:
    """Get the name of the user from the file path provided, from a json file."""
    try:
        with open(file_path, "r") as f:
            name: str = json.load(f)["name"]
        return name

    except KeyError:
        with open(file_path, "w") as f:
            json.dump({"name": ""}, f)
        return None

def set_name(name: str, file_path: str) -> None:
    """Set the name of the user in the file path provided, in a json file."""
    try:
        with open(file_path, "w") as f:
            json.dump({"name": name}, f)

    except FileNotFoundError:
        print("Invalid or non existant directory or file path provided.")
    except KeyError:
        print("Invalid json file provided.")
