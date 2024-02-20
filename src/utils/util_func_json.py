import json
from const import ENC_TYPE


def save_json_result(path: str, obj: dict):
    with open(path, "w", encoding = ENC_TYPE) as fp:
        json.dump(
            obj = obj, 
            fp = fp, 
            indent = 4,
            sort_keys = True, 
            ensure_ascii = False
        )
        
        
        
def read_json_result(path: str):
    with open(path, "r", encoding = ENC_TYPE) as fp:
        result = json.load(fp)
        
    return result