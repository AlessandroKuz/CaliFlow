import datetime
import time

from utils.settings import PERSONAL_DATA_FILE_PATH, WORKOUT_TYPES, USER_TYPE, APP_NAME, WORKOUT_DATA_FILE_PATH
from user import user_greeting, files_setup

"""
IDEA:
-Setup:
    Get username, optional(age, height, weight)
-App:
    Get type of workout
    --> get exercise(s)
    --> get reps and sets (number or duration)
    --> write to file
"""

"""
TODO: CREATE A PROPER APP PATH:
\CaliFlow
    \Data
        -Username   OR  Setting.ini ?
        -Workouts
    \Scripts
        -CaliFlow.py
        -Log.log    ???

IF FILES NOT SET UP THEN RUN SCRIPT THAT CREATES ALL NECESSARY DIRS AND FILES
"""

# TODO: Reps don't make any sense for time exercises (ex: Planks)!!!
# Can't Create directory with file write - only file
# Check, if new guy 1 type of execution, if already member other execution


def main(user_type: str) -> None:
    workout_type: str | None = workout_chooser(user_type)
    if workout_type:
        exercise_list: list[str] = get_all_exercises()
        print_all_exercises(exercise_list)
        routine: str | list[str] | None = choosing_routine(exercise_list, workout_type)        
        if routine:
            track_workout(routine)


def workout_chooser(user_type: str) -> str | None:
    choosing_workout_type: bool = True
    chosen_workout: str = ""

    if user_type == USER_TYPE[0]:
        print("TUTORIAL: \nYou can either choose all your exercises togheter", 
              "or one at a time.", end=" ")
        input_text: str = """Which type of workout would you like to do today?
        (type in 1 to choose multiple exercises all at once | type in 2 to choose only a single exercise): """
    else:
        input_text = "What type of workout would you like to do today? (1 or 2): "

    while choosing_workout_type:
        try:
            workout_type = int(input(input_text))
            if workout_type in [1, len(WORKOUT_TYPES)]:
                chosen_workout = WORKOUT_TYPES[workout_type - 1]
                choosing_workout_type = False
            elif workout_type < 1:
                quit_confirmation: str = input("Do you really wanna quit (y/n)? ").lower()
                if quit_confirmation == "y" or quit_confirmation == "yes":
                    return None
            else:
                raise ValueError
        except ValueError:
            print("The value must a number between",
                  f"1 and {len(WORKOUT_TYPES)}")
    
    return chosen_workout


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
    

def print_exercise_guide(quit_value: int):
    print("Choose a list of exercises you would like to perform",
          f"when done input {quit_value}.\n")


def choosing_routine(exercise_list: list[str],
             workout_type: str) -> list[str] | str | None:
    
    quit_value: int = 0
    total_exercises_num: int = len(exercise_list)
    choosing_exercises: bool = True
    workout_list: list[str] = []
    input_message = "Which exercise would you like to add?" \
                    if workout_type == WORKOUT_TYPES[0] \
                    else "Which exercise would you like to perform?"
    
    print_exercise_guide(quit_value)

    while choosing_exercises:
        try:
            exercise_num = int(input(f"{input_message} "))
            if exercise_num == quit_value:
                choosing_exercises = False
            elif 1 <= exercise_num <= total_exercises_num:
                chosen_exercise: str = exercise_list[exercise_num - 1]
                print(f"You added {chosen_exercise} to your workout.")
                workout_list.append(chosen_exercise)
                if workout_type == WORKOUT_TYPES[1]:
                    choosing_exercises = False
            else:
                raise ValueError

        except ValueError:
            print("Invalid input, type in a number between",
                f"1 and {total_exercises_num} to choose the exercise;\n",
                f"press {quit_value} to exit input.")
    
    if workout_list:
        return workout_list if workout_type == WORKOUT_TYPES[0] else workout_list[0]
    return None


def track_workout(routine: str | list[str]):
    date = datetime.datetime.today().strftime("%d/%m/%Y")

    if not isinstance(routine, list):
        routine = [routine]

    write_date(date)
    for exercise in routine:
        print(f"You are now tracking {exercise}:")
        output = track_exercise(exercise)
        print(output)
        with open (WORKOUT_DATA_FILE_PATH, "a") as f:
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
                str_sets: str = ", ".join([str(set) for set in sets])
                print(f"Sets: {str_sets}")

        except ValueError:
            print("Invalid input, type in a valid number.")
    
    end_datetime = datetime.datetime.now()

    time_difference = end_datetime - start_datetime

    hours: int = time_difference.seconds // 3600
    minutes: int = (time_difference.seconds % 3600) // 60
    seconds: int = time_difference.seconds % 60

    start_time = start_datetime.strftime("%H:%M")
    end_time = end_datetime.strftime("%H:%M")

    str_sets: str = ", ".join([str(set) for set in sets])

    time: str = f"Time: {start_time} -> {end_time},"
    sets_done: str = f"{len(sets)} Sets: {str_sets}."
    exercise_sets: str = f"{exercise}:\n\t\t{sets_done}"
    hours_duration: str = f"{hours}h:" if hours != 0 else ""
    minutes_duration: str = f"{minutes}m:" if minutes != 0 else ""
    seconds_duration: str = f"{seconds}s"
    duration: str = hours_duration + minutes_duration + seconds_duration

    exercise_output: str = f"\t{time}\n" + \
                f"\t{exercise_sets}\n\tIt took you {duration} to finish.\n\n"
    
    return exercise_output


def write_date(date: str):
    with open (WORKOUT_DATA_FILE_PATH, "a") as f:
        f.write(f"{date}\n")


if __name__ == "__main__":
    files_setup()
    user_type = user_greeting()
    time.sleep(1)
    main(user_type=user_type)
