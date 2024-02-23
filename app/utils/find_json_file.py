import glob
import os


def find_json_file(directory="app/data") -> str:
    json_files = glob.glob(os.path.join(directory, "*.json"))
    if not json_files:
        raise FileNotFoundError("No JSON file found in the specified directory.")
    return json_files[0]
