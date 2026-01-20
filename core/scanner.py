from modules.geo import get_geo_info
from modules.carrier import get_carrier_info
from modules.osint import get_osint_links
from modules.voip import is_voip
from modules.risk import calculate_risk

def scan_number(parsed):
    geo = get_geo_info(parsed)
    carrier = get_carrier_info(parsed)
    voip = is_voip(parsed)
    risk = calculate_risk(voip, carrier)
    osint = get_osint_links(parsed)

    return geo, carrier, voip, risk, osint
