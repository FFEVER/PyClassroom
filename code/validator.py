def is_valid_string(s):
    return type(s) == str and s != ""

def is_valid_int(s):
    try:
        s = int(s)
        return s > 0
    except ValueError:
        return False
    
