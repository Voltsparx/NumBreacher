from phonenumbers import geocoder, timezone

def get_geo_info(parsed):
    return {
        "Country": geocoder.country_name_for_number(parsed, "en"),
        "Region": geocoder.description_for_number(parsed, "en"),
        "Timezone": ", ".join(timezone.time_zones_for_number(parsed))
    }
