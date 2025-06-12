#415-222-1223
def is_phone_no(text):
    if len(text) != 12:
        return False


    for i in range(0,3):
        if not text[i].isnumeric():
            return False

    if text[3] != '-' or text[7] != '-'  :
        return False

    for i in range(4,6):
        if not text[i].isnumeric():
            return False

    for i in range(8,12):
        if not text[i].isnumeric():
            return False

    return True

print(f"is +9112345678 is a valid number? {is_phone_no("123-222-2345")}" )
