def main(write_to_file: bool=False):
    """Function that lets you track how many reps and set have you done of a 
     given excercise, optional output file"""

    excercise_list: list[str] = [
        "Push-up",
        "Pull-up",
        "Chin-up",
        "Dip",
        "Military-press",
        "Curl",
        "Plank",
        "Bridge",
        "Squat",
        "Calf raise"
        ]
    total_exercises_num: int = len(excercise_list)
    chosen_exercise: str = ""

    while True:
        print("Excercise list:")
        for index, exercise in enumerate(excercise_list, start=1):
            print(f"{index}. {exercise}")
        
        # Asking for the exercise
        while True:
            try:
                exercise_num: int = int(input("Which exercise would you like to do? "))
                if exercise_num == 0:
                    break
                if 1 <= exercise_num <= total_exercises_num:
                    chosen_exercise = excercise_list[exercise_num - 1]
                    print(f"You chose {chosen_exercise}.")
                    break
                raise ValueError
            except ValueError:
                print("Invalid input, type in a number between",
                    f"1 and {total_exercises_num} to choose the exercise.""")
        
        if exercise_num == 0:
            break

        # questo deve solo partire se sopra hanno scelto l'esercizio
        # Asking for reps & sets
        if chosen_exercise: 
            sets: list = []
            while True:
                try:
                    repetitions: int = int(input("How many reps have done on this set? "))
                    if repetitions < 1:
                        break
                    elif 1 <= repetitions:
                        sets.append(repetitions)
                        print(sets)
                        # if write_to_file:
                        #     with open("exercises.txt", "a") as f:
                        #         f.write(f"{chosen_exercise}")
                    else:
                        raise ValueError
                except ValueError:
                    print("Invalid input, type in a valid number.")
            
            if write_to_file:
                with open("exercises.txt", "w") as f:
                    f.write(f"{chosen_exercise}:\n\t{len(sets)} Sets: {sets}.")


if __name__ == "__main__":
    main(True)