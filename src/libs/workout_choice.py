from utils.settings import WORKOUT_TYPES, USER_TYPE


def workout_chooser(user_type: str) -> str:
    choosing_workout_type: bool = True
    chosen_workout: str = ""

    if user_type == USER_TYPE[0]:
        print("TUTORIAL: \nYou can either choose all your exercises togheter", 
              "or one at a time.", end=" ")
        input_text: str = """Which type of workout would you like to do today?
        (type in 1 to choose multiple exercises all at once | type in 2 to choose only a single exercise): """
    else:
        input_text = "What type of workout would you like to do today (multiple exercises or a single one? -> 1 or 2): "

    while choosing_workout_type:
        try:
            workout_type = int(input(input_text))
            if workout_type in [1, len(WORKOUT_TYPES)]:
                chosen_workout = WORKOUT_TYPES[workout_type - 1]
                choosing_workout_type = False
            elif workout_type < 1:
                quit_confirmation: str = input("Do you really wanna quit (y/n)? ").lower()
                if quit_confirmation in ["y", "yes", "0"]:
                    print("Bye!")
                    exit()
            else:
                raise ValueError
        except ValueError:
            print("The value must a number between",
                  f"1 and {len(WORKOUT_TYPES)}")
    
    return chosen_workout


def routine_chooser(exercise_list: list[str],
             workout_type: str) -> list[str]:
    
    quit_value: int = 0
    total_exercises_num: int = len(exercise_list)
    choosing_exercises: bool = True
    workout_list: list[str] = []
    input_message = "Which exercise would you like to add to your workout?" \
                    if workout_type == WORKOUT_TYPES[0] \
                    else "Which exercise would you like to perform?"
    
    exercise_guide(quit_value)

    while choosing_exercises:
        try:
            exercise_num = int(input(f"{input_message} "))
            if exercise_num == quit_value:
                choosing_exercises = False
            elif 1 <= exercise_num <= total_exercises_num:
                chosen_exercise: str = exercise_list[exercise_num - 1]
                print(f"You added {chosen_exercise} to your workout.\n")
                workout_list.append(chosen_exercise)
                if workout_type == WORKOUT_TYPES[1]:
                    choosing_exercises = False
            else:
                raise ValueError

        except ValueError:
            print("Invalid input, type in a number between",
                f"1 and {total_exercises_num} to choose the exercise;\n",
                f"press {quit_value} to exit input.\n")
    
    if not workout_list:
        print("Bye!")
        exit()

    return workout_list


def exercise_guide(quit_value: int):
    print("\n\tChoose a list of exercises you would like to perform",
          f"when done input {quit_value}.\n\n")
