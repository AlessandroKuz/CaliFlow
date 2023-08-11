from datetime import datetime as dt

from utils.settings import WORKOUT_DATA_FILE_PATH


def track_workout(routine: list[str]):
    date = dt.today().strftime("%d/%m/%Y")

    write_date(date)
    print("-"*100)
    for exercise in routine:
        print(f"You are now tracking {exercise}:")
        output = track_exercise(exercise)
        print(output)
        with open(WORKOUT_DATA_FILE_PATH, "a") as f:
            f.write(f"{output}")
    

def track_exercise(exercise: str) -> str:
    start_datetime = dt.now()
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
                print(f"Sets: {str_sets}\n")

        except ValueError:
            print("Invalid input, type in a valid number.")
    
    end_datetime = dt.now()

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
        f.write(f"Date: {date}\n")
