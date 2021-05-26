import re

def is_valid_lot_number(number:int) -> bool:
    return 0 < number < 100

def is_valid_postal_code(code:str) -> bool:
    return bool(re.search("[a-z0-9]{1,4}", code))

def is_valid_owner_name(name:str) -> bool:
    return len(name) < 128
