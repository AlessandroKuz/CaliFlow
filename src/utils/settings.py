from utils.get_path import get_path


APP_NAME: str = "CaliFlow"
FILE_NAME: str = "exercises.txt"
DEFAULT_PATH: str = get_path(__file__)
DEFAULT_FILE_PATH: str = f"{DEFAULT_PATH}/{FILE_NAME}"
WORKOUT_TYPES: tuple[str, str] = ("Complex workout", "Simple workout")
USER_TYPE: tuple[str, str] = ("New user", "Existing user")
