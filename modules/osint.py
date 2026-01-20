def get_osint_links(parsed):
    num = str(parsed.country_code) + str(parsed.national_number)

    return {
        "Truecaller": f"https://www.truecaller.com/search/{parsed.country_code}/{num}",
        "Google": f"https://www.google.com/search?q={num}",
        "Facebook": f"https://www.facebook.com/search/top/?q={num}",
        "WhatsApp": f"https://wa.me/{num}",
        "Telegram": f"https://t.me/{num}"
    }
