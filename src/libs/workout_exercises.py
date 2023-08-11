import time

from utils.settings import EXERCISES_FILE_PATH


def get_all_exercises() -> list[str]:
    with open(EXERCISES_FILE_PATH, "r") as file:
        return file.read().split(", ")


def print_all_exercises(exercise_list: list[str]) -> None:
    # In case the file is empty or contains only empty strings
    if len(exercise_list) == 0 or exercise_list == [""]:
        print("\nNo exercises found, an error likely accurred.",
              "Please restart the program to generate the default exercises.",
              sep="\n")
        exit(-1)
    
    print("Excercise list:")
    for index, exercise in enumerate(exercise_list, start=1):
        
        # TODO: Check if powershell is used then use time.sleep(0.1), else use time.sleep(0.5)
        time.sleep(0.1)
        print(f"{index}. {exercise}")
    print()
    