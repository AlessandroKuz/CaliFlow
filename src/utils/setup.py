import os
from utils.settings import DATA_FOLDER_PATH, PERSONAL_DATA_FILE_PATH, WORKOUT_DATA_FILE_PATH


def check_for_necessary_files() -> dict[str, bool]:
    """Checks whether the necessary files and directories are present."""
    necessary_files: dict[str, bool] = {
        "data_folder": True,  # Folder containing all data files
        "data_file": True,  # File containing user's data
        "workout_data_file": True,  # File containing all tracked workouts
    }
    if not os.path.isdir(DATA_FOLDER_PATH):
        necessary_files["data_folder"] = False
    
    if not os.path.isfile(PERSONAL_DATA_FILE_PATH):
        necessary_files["data_file"] = False

    if not os.path.isfile(WORKOUT_DATA_FILE_PATH):
        necessary_files["workout_data_file"] = False

    return necessary_files


def create_missing_files(necessary_files: dict[str, bool]) -> None:
    """Creates the missing files."""
    if necessary_files["data_folder"] == False:
        os.mkdir(DATA_FOLDER_PATH)

    if necessary_files["data_file"] == False:
        with open(PERSONAL_DATA_FILE_PATH, "w") as f:
            f.write("{}")

    if necessary_files["workout_data_file"] == False:
        with open(WORKOUT_DATA_FILE_PATH, "w") as f:
            f.write("{}")
