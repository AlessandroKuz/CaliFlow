import datetime


APP_NAME: str = "CaliFlow"
DEFAULT_FILE_PATH: str = "exercises.txt"


def welcome(file_path: str | None = None) -> str | None:
    if file_path:
        try:
            with open(file_path, "r") as f:
                name: str = f.readline().strip()
                if name:
                    print(f"Hello {name}! Welcome back!")
                    return name
        except FileNotFoundError:
            print("Invalid directory or file path provided.")
        
    print(f"Hi! Welcome to {APP_NAME}")
    name: str = input("What's your name? ")
    with open(DEFAULT_FILE_PATH, "w") as f:
        f.write(f"{name}\n\n")
    print(f"Your account has been setup, Hello {name}!")
    

def main(log_to_file: bool = False, file_path: str = "exercises.txt"):
    type_of_workout: str = workout_chooser()
    if type_of_workout:
        routine: str | list[str] | None = get_routine(type_of_workout)
        if routine:
            track_workout(routine, log_to_file, file_path)


def workout_chooser() -> str:
    workout_types: tuple[str, str] = ("complex workout", "simple workout")
    choosing_workout_type: bool = True
    chosen_workout: str = ""

    print("You can either choose all your exercises togheter", 
          "or one at a time.", end=" ")

    while choosing_workout_type:
        try:
            workout_type = int(input("What would you like to do? (1 or 2): "))
            if workout_type in [1, len(workout_types)]:
                chosen_workout = workout_types[workout_type - 1]
                choosing_workout_type = False
            else:
                raise ValueError
        except ValueError:
            print("The value must a number between",
                  f"1 and {len(workout_types)}")
    
    return chosen_workout


def get_routine(type: str) -> str | list[str] | None:
    routine: str | list[str] | None = ""
    exercise_list: list[str] = get_all_exercises()
    print_all_exercises(exercise_list)

    if type == "complex workout":
        routine = choose_exercise_list(exercise_list)
    elif type == "simple workout":
        routine = choose_exercise(exercise_list)
    
    return routine


def get_all_exercises() -> list[str]:
    return ["Push-up",
            "Pull-up",
            "Chin-up",
            "Dip",
            "Military-press",
            "Curl",
            "Plank",
            "Bridge",
            "Squat",
            "Calf raise"]


def print_all_exercises(exercise_list: list[str]) -> None:
    print("Excercise list:")
    for index, exercise in enumerate(exercise_list, start=1):
        print(f"{index}. {exercise}")
    

def choose_exercise_list(exercise_list: list[str]) -> list[str] | None:
    total_exercises_num: int = len(exercise_list)
    workout_list: list[str] = []
    choosing_exercises: bool = True
    quit_value: int = 0
    
    print("Choose a list of exercises you would like to do",
          f"when done input {quit_value}.")

    while choosing_exercises:
        try:
            exercise_num = int(input("Which exercise would you like to do? "))
            if exercise_num == quit_value:
                choosing_exercises = False
            elif 1 <= exercise_num <= total_exercises_num:
                chosen_exercise: str = exercise_list[exercise_num - 1]
                print(f"You added {chosen_exercise} to your workout.")
                workout_list.append(chosen_exercise)
            else:
                raise ValueError

        except ValueError:
            print("Invalid input, type in a number between",
                f"1 and {total_exercises_num} to choose the exercise;\n",
                f"press {quit_value} to exit input.")
    
    return workout_list


def choose_exercise(exercise_list: list[str]) -> str | None:
    total_exercises_num: int = len(exercise_list)
    chosen_exercise: str = ""
    choosing_exercise: bool = True
    quit_value: int = 0
    
    print("Choose an exercise you would like to do",
          f"or input {quit_value} to exit.")

    while choosing_exercise:
        try:
            exercise_num = int(input("Which exercise would you like to do? "))
            if exercise_num == quit_value:
                choosing_exercise = False
            elif 1 <= exercise_num <= total_exercises_num:
                chosen_exercise: str = exercise_list[exercise_num - 1]
                print(f"You choose {chosen_exercise}.")
                choosing_exercise = False
            else:
                raise ValueError

        except ValueError:
            print("Invalid input, type in a number between",
                f"1 and {total_exercises_num} to choose the exercise;\n",
                f"press {quit_value} to exit input.")
    
    if not choosing_exercise:
        return chosen_exercise


def track_workout(routine: str | list[str],
                  output_file: bool = False,
                  file_path: str = "exercises.txt"):

    if isinstance(routine, list):
        write_date(file_path)
        for exercise in routine:
            print(f"You are now tracking {exercise}:")
            output = track_exercise(exercise)
            print(output)
            if output_file:
                with open (file_path, "a") as f:
                    f.write(f"{output}")
    
    else:
        write_date(file_path)
        output = track_exercise(routine)
        print(output)
        if output_file:
            with open (file_path, "a") as f:
                f.write(f"{output}")


def track_exercise(exercise: str) -> str:
    start_datetime = datetime.datetime.now()
    sets: list[int] = []
    tracking_reps: bool = True
    quit_value = 0

    print("Type in your reps per set,", 
          f"when done type in a value below {quit_value + 1}.")

    while tracking_reps:
        try:
            repetitions = int(input("How many reps have you done this set? "))
            if repetitions <= quit_value:
                tracking_reps = False
            else:
                sets.append(repetitions)
                print(sets)

        except ValueError:
            print("Invalid input, type in a valid number.")
    
    end_datetime = datetime.datetime.now()

    time_difference = end_datetime - start_datetime

    hours: int = time_difference.seconds // 3600
    minutes: int = (time_difference.seconds % 3600) // 60
    seconds: int = time_difference.seconds % 60

    start_time = start_datetime.strftime("%H:%M")
    end_time = end_datetime.strftime("%H:%M")

    time: str = f"Time: {start_time} -> {end_time},"
    sets_done: str = f"{len(sets)} Sets: {sets}."
    exercise_sets: str = f"{exercise}:\n\t\t{sets_done}"
    hours_duration: str = f"{hours}h:" if hours != 0 else ""
    minutes_duration: str = f"{minutes}m:" if minutes != 0 else ""
    seconds_duration: str = f"{seconds}s"
    duration: str = hours_duration + minutes_duration + seconds_duration

    exercise_output: str = f"\t{time}\n" + \
                f"\t{exercise_sets}\n\tIt took you {duration} to finish.\n\n"
    
    return exercise_output


def write_date(file_path: str):
    date = datetime.datetime.today().strftime("%d/%m/%Y")
    with open (file_path, "a") as f:
            f.write(f"Date: {date}\n")


if __name__ == "__main__":
    file_path = DEFAULT_FILE_PATH
    welcome(file_path)
    main(log_to_file=True)
