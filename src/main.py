import time
from random import choice

from utils.settings import APP_NAME
from libs.user import user_greeting, files_setup
from libs.workout_exercises import print_all_exercises, get_all_exercises
from libs.workout_choice import workout_chooser, routine_chooser
from libs.workout_track import track_workout


def main() -> None:
    files_setup()
    print("="*60, f"\t\t\t{APP_NAME} v0.1", "="*60, sep="\n", end="\n\n")
    user_type = user_greeting()
    time.sleep(0.5)

    workout_type: str = workout_chooser(user_type)
    if workout_type:
        exercise_list: list[str] = get_all_exercises()
        print_all_exercises(exercise_list)
        routine: list[str] = routine_chooser(exercise_list, workout_type)        
        if routine:
            track_workout(routine)
            time.sleep(0.5)
            # TODO: Add a function to print a summary of the workout
            print(f"Congratulations!", end="") 
            time.sleep(0.2)
            print("\N{clapping hands sign}", end="")
            time.sleep(0.2)
            print("You've completed your workout!")
            time.sleep(0.2)
            print("\N{flexed biceps}", end="\n\n")
            time.sleep(1)


        goodbye_message: list[str] = [
            "Bye!\N{WAVING HAND SIGN}",
            "Goodbye!\N{WAVING HAND SIGN}",
            "See you!\N{WAVING HAND SIGN}",
            "See you soon!\N{WAVING HAND SIGN}",
            "See you next time!\N{WAVING HAND SIGN}"
        ]
        print(choice(goodbye_message), end="\n\n")
        print()

if __name__ == "__main__":
    main()
