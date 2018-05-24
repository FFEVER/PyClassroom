def is_valid_string(s):
    return type(s) == str and s != ""

def is_valid_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    