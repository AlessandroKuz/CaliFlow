from utils.get_path import get_path


APP_NAME: str = "CaliFlow"
PERSONAL_DATA_FILE_NAME: str = "personal_data.json"
DATA_FOLDER_NAME: str = "data"
PROJECT_PATH: str = get_path()
DEFAULT_FILE_PATH: str = f"{PROJECT_PATH}/{DATA_FOLDER_NAME}/{PERSONAL_DATA_FILE_NAME}"
WORKOUT_TYPES: tuple[str, str] = ("Complex workout", "Simple workout")
USER_TYPE: tuple[str, str] = ("New user", "Existing user")
