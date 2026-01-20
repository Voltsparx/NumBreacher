from phonenumbers import number_type, PhoneNumberType

def is_voip(parsed):
    return number_type(parsed) == PhoneNumberType.VOIP
