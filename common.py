from enum import Enum
import json

class DataFile(Enum):
    Valid = 1
    Invalid = 2


def get_filename(type:DataFile) -> str:
    return {
        DataFile.Valid: "./data/valid.json",
        DataFile.Invalid: "./data/invalid.json"
    }[type]

def load_data(type:DataFile) -> dict:
    filename = get_filename(type)

    if len(filename):
        with open(filename) as file:
            contents = str(file.read())
            return json.loads(contents) if len(contents) else {}
    
    return {}
