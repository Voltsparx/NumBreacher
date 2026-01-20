from utils.colors import CYAN, RESET

def format_output(number, geo, carrier, voip, risk, osint):
    out = []
    out.append(f"{CYAN}Scan Result for {number}{RESET}")
    out.append("-" * 40)

    for k, v in geo.items():
        out.append(f"{k:12}: {v}")

    out.append(f"Carrier     : {carrier}")
    out.append(f"VoIP        : {'Yes' if voip else 'No'}")
    out.append(f"Risk Level  : {risk}")

    out.append("\nOSINT Links:")
    for name, link in osint.items():
        out.append(f" {name:10}: {link}")

    return "\n".join(out)
