from utils.get_path import get_path


APP_NAME: str = "CaliFlow"
PERSONAL_DATA_FILE_NAME: str = "personal_data.json"
WORKOUT_DATA_FILE_NAME: str = "workout_data.txt"
DATA_FOLDER_NAME: str = "data"
CURRENT_MAIN_PATH: str = get_path()
DATA_FOLDER_PATH: str = f"{CURRENT_MAIN_PATH}\\{DATA_FOLDER_NAME}"
PERSONAL_DATA_FILE_PATH: str = f"{DATA_FOLDER_PATH}\\{PERSONAL_DATA_FILE_NAME}"
WORKOUT_DATA_FILE_PATH: str = f"{DATA_FOLDER_PATH}\\{WORKOUT_DATA_FILE_NAME}"
WORKOUT_TYPES: tuple[str, str] = ("Complex workout", "Simple workout")
USER_TYPE: tuple[str, str] = ("New user", "Existing user")
