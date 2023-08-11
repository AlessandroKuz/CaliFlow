import os
from utils.settings import DATA_FOLDER_PATH, PERSONAL_DATA_FILE_PATH, WORKOUT_DATA_FILE_PATH, EXERCISES_FILE_PATH


def check_for_necessary_files() -> dict[str, bool]:
    """Checks whether the necessary files and directories are present."""
    necessary_files: dict[str, bool] = {
        "data_folder": False,  # Folder containing all data files
        "data_file": False,  # File containing user's data
        "workout_data_file": False,  # File containing all tracked workouts
        "exercise_data_file": False,  # File containing all default exercises
    }
    # check if the data folder exists
    if os.path.exists(DATA_FOLDER_PATH) and \
       os.path.isdir(DATA_FOLDER_PATH):
        necessary_files["data_folder"] = True
    
    if os.path.exists(PERSONAL_DATA_FILE_PATH) and \
       os.path.isfile(PERSONAL_DATA_FILE_PATH):
        necessary_files["data_file"] = True

    if os.path.exists(WORKOUT_DATA_FILE_PATH) and \
       os.path.isfile(WORKOUT_DATA_FILE_PATH):
        necessary_files["workout_data_file"] = True

    if os.path.exists(EXERCISES_FILE_PATH) and \
       os.path.isfile(EXERCISES_FILE_PATH) and \
       os.path.getsize(EXERCISES_FILE_PATH) != 0:
        necessary_files["exercise_data_file"] = True

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
            f.write("")

    if necessary_files["exercise_data_file"] == False:
        with open(EXERCISES_FILE_PATH, "w") as f:
            default_exercises: list[str] = [
                "Pull-ups",
                "Chin-ups",
                "Dips",
                "Push-ups",
                "Military press",
                "Bicep curls",
                "Squats",
                "Lunges",
                "Sit-ups",
                "Plank",
                "Leg raises",
                "Calf raises",
                "Glute bridge",
                "Hollow body hold"]
            f.write(", ".join(default_exercises))