from utils.settings import PERSONAL_DATA_FILE_PATH, USER_TYPE, APP_NAME

from utils.setup import check_for_necessary_files, create_missing_files
from utils.name import get_name, set_name


def files_setup():
    """Checks whether the necessary files and directories are present.
    If not, creates them."""
    necessary_files: dict[str, bool] = check_for_necessary_files()
    create_missing_files(necessary_files)


def user_greeting() -> str:
    """Greet the user, ask for their name if not registered.
    Return the user type (new or existing)."""
    name: str = get_name(PERSONAL_DATA_FILE_PATH)
    if not name:
        print(f"Welcome to {APP_NAME}!")
        name: str = input("What's your name? ").title()
        set_name(name, PERSONAL_DATA_FILE_PATH)
        print(f"Your account has been setup. Hello {name}!")
        # create a wrapper function - if new user run set up file
        files_setup()
        return USER_TYPE[0]  # if new user run set up file
    
    print(f"Welcome back {name}!")
    # create a wrapper function - if existing user run app file
    # check for files integrity??? - or run the app then check for files integrity
    return USER_TYPE[1]  
