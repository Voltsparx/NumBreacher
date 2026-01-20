import phonenumbers

def validate_number(number):
    try:
        parsed = phonenumbers.parse(number)
        return phonenumbers.is_valid_number(parsed), parsed
    except:
        return False, None
