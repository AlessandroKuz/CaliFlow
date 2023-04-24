import datetime


def main(log_to_file: bool = False):
    """Function that lets you track how many reps and set have you done of a
        given exercise, optional output file"""
    exercise: str | None = choose_exercise()
    if exercise:
        track_exercise(exercise, log_to_file)


def choose_exercise() -> str | None:
    """Function that lets you choose an exercise from a list of exercises"""
    exercises: list[str] = get_all_exercises()
    print_all_exercises(exercises)
    chosen_exercise: str | None = getting_valid_exercise(exercises)
    if chosen_exercise:
        return chosen_exercise


def track_exercise(exercise: str, write_to_file: bool = False):
    """Function that lets you track how many reps and set have you done of a 
     given exercise, optional output file"""
    start_datetime = datetime.datetime.now()
    sets: list[int] = []
    while True:
        try:
            repetitions: int = int(input("How many reps have you done on this set? "))
            if repetitions < 1:
                break
            elif 1 <= repetitions:
                sets.append(repetitions)
                print(sets)
            else:
                raise ValueError

        except ValueError:
            print("Invalid input, type in a valid number.")
    
    if write_to_file:
        end_datetime = datetime.datetime.now()

        time_difference = end_datetime - start_datetime

        # BUG IF INPUT 4 IT CHOOSES DIPS BUT SAYS INVALID INPUT

        # Extract the time difference in hours, minutes, and seconds
        hours = time_difference.seconds // 3600
        minutes = (time_difference.seconds % 3600) // 60
        seconds = time_difference.seconds % 60

        # subtracting end time (time) from start time (start_time) to get total time

        date = start_datetime.strftime("%d/%m/%Y")
        start_time = start_datetime.strftime("%H:%M")
        end_time = end_datetime.strftime("%H:%M")

        with open("exercises.txt", "a") as f:
            f.write(f"""Date: {date} Time: {start_time} -> {end_time}\n{exercise}:\n\t{len(sets)} Sets: {sets}.\nIt took you {f"{hours}h:" if hours != 0 else ""}{f"{minutes}m:" if minutes != 0 else ""}{seconds}s to finish.\n""")


def get_all_exercises() -> list[str]:
    exercise_list: list[str] = [
        "Push-up",
        "Pull-up",
        "Chin-up",
        "Dip",
        "Military-press",
        "Curl",
        "Plank",
        "Bridge",
        "Squat",
        "Calf raise"]

    return exercise_list


def print_all_exercises(exercise_list: list[str]) -> None:
    print("Excercise list:")
    for index, exercise in enumerate(exercise_list, start=1):
        print(f"{index}. {exercise}")
    

def getting_valid_exercise(exercise_list: list[str]) -> str | None:
    total_exercises_num: int = len(exercise_list)
    chosen_exercise: str = ""
    chosen_valid_exercise: bool = False
    quit_value: int = 0

    while not chosen_valid_exercise:
        try:
            exercise_num: int = int(input("Which exercise would you like to do? "))
            if exercise_num == quit_value:
                break
            elif 1 <= exercise_num <= total_exercises_num:
                chosen_exercise: str = exercise_list[exercise_num - 1]
                print(f"You chose {chosen_exercise}.")
                chosen_valid_exercise = True
            else:
                raise ValueError

        except ValueError:
            print("Invalid input, type in a number between",
                f"1 and {total_exercises_num} to choose the exercise.""")
    
    if chosen_valid_exercise:
        return chosen_exercise


if __name__ == "__main__":
    main(log_to_file = True)
