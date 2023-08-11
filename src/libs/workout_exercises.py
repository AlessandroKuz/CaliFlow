def get_all_exercises() -> list[str]:
    return ["Push-ups",
            "Pull-ups",
            "Chin-ups",
            "Dips",
            "Military-presses",
            "Curls",
            "Plank",
            "Bridges",
            "Squats",
            "Calf raises"]


def print_all_exercises(exercise_list: list[str]) -> None:
    print("Excercise list:")
    for index, exercise in enumerate(exercise_list, start=1):
        print(f"{index}. {exercise}")
    print()
    