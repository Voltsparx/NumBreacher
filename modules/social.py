import urllib.parse

SOCIAL_PLATFORMS = {
    "Facebook": "https://www.facebook.com/search/top?q={}",
    "Twitter/X": "https://twitter.com/search?q={}",
    "Instagram": "https://www.instagram.com/accounts/search/?q={}",
    "LinkedIn": "https://www.linkedin.com/search/results/all/?keywords={}",
    "Telegram": "https://t.me/{}",
    "TrueCaller": "https://www.truecaller.com/search/{}"
}

def get_social_links(number):
    links = {}
    clean = number.replace("+", "").replace(" ", "")

    for platform, url in SOCIAL_PLATFORMS.items():
        encoded = urllib.parse.quote(clean)
        links[platform] = url.format(encoded)

    return links
