from utils.get_path import get_path


APP_NAME: str = "CaliFlow"
DATA_FILE_NAME: str = "personal_data.json"
DATA_FOLDER_NAME: str = "data"
DEFAULT_PATH: str = get_path()
DEFAULT_FILE_PATH: str = f"{DEFAULT_PATH}/{DATA_FOLDER_NAME}/{DATA_FILE_NAME}"
WORKOUT_TYPES: tuple[str, str] = ("Complex workout", "Simple workout")
USER_TYPE: tuple[str, str] = ("New user", "Existing user")
