from phonenumbers import carrier

def get_carrier_info(parsed):
    try:
        name = carrier.name_for_number(parsed, "en")
        return name if name else "Unknown"
    except:
        return "Unknown"
