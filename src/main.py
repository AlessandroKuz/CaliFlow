import time

from utils.settings import APP_NAME
from libs.user import user_greeting, files_setup
from libs.workout_exercises import print_all_exercises, get_all_exercises
from libs.workout_choice import workout_chooser, routine_chooser
from libs.workout_track import track_workout


def main() -> None:
    print("="*60, f"\t\t\t{APP_NAME}" " v0.1", "="*60, sep="\n", end="\n"*2)
    files_setup()
    time.sleep(0.8)
    user_type = user_greeting()
    time.sleep(0.5)

    workout_type: str = workout_chooser(user_type)
    if workout_type:
        exercise_list: list[str] = get_all_exercises()
        print_all_exercises(exercise_list)
        routine: list[str] = routine_chooser(exercise_list, workout_type)        
        if routine:
            track_workout(routine)

if __name__ == "__main__":
    main()
