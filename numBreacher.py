from banner import show_banner
from core.validator import validate_number
from core.scanner import scan_number
from core.formatter import format_output
from utils.helpers import save_result

def help_menu():
    print("""
Commands:
 scan <number>     Scan a phone number
 help              Show this menu
 exit              Exit tool
""")

def shell():
    show_banner()
    help_menu()

    while True:
        cmd = input("\nNumBreacher > ").strip()

        if cmd == "exit":
            break

        elif cmd == "help":
            help_menu()

        elif cmd.startswith("scan"):
            parts = cmd.split()
            if len(parts) < 2:
                print("Usage: scan <number>")
                continue

            number = parts[1]
            valid, parsed = validate_number(number)

            if not valid:
                print("Invalid number.")
                continue

            geo, carrier, osint = scan_number(parsed)
            output = format_output(number, geo, carrier, osint)
            print(output)
            save_result(output)

        else:
            print("Unknown command. Type 'help'.")

if __name__ == "__main__":
    shell()
import json
from banner import show_banner
from core.validator import validate_number
from core.scanner import scan_number
from core.formatter import format_output
from utils.helpers import save_result

def help_menu():
    print("""
Commands:
 scan <number>           Scan a phone number
 bulk <file.txt>         Scan multiple numbers
 exportjson <file.json>  Export last results to JSON
 help                    Show this menu
 exit                    Exit tool
""")

last_results = []

def shell():
    global last_results
    show_banner()
    help_menu()

    while True:
        cmd = input("\nNumBreacher > ").strip()

        if cmd == "exit":
            break

        elif cmd == "help":
            help_menu()

        elif cmd.startswith("scan"):
            parts = cmd.split()
            if len(parts) < 2:
                print("Usage: scan <number>")
                continue

            number = parts[1]
            valid, parsed = validate_number(number)
            if not valid:
                print("Invalid number.")
                continue

            geo, carrier, voip, risk, osint = scan_number(parsed)
            output = format_output(number, geo, carrier, voip, risk, osint)
            print(output)
            save_result(output)

            last_results.append({
                "number": number,
                "geo": geo,
                "carrier": carrier,
                "voip": voip,
                "risk": risk,
                "osint": osint
            })

        elif cmd.startswith("bulk"):
            parts = cmd.split()
            if len(parts) < 2:
                print("Usage: bulk <file.txt>")
                continue

            try:
                with open(parts[1]) as f:
                    for line in f:
                        number = line.strip()
                        if not number:
                            continue
                        valid, parsed = validate_number(number)
                        if valid:
                            geo, carrier, voip, risk, osint = scan_number(parsed)
                            output = format_output(number, geo, carrier, voip, risk, osint)
                            print(output)
                            save_result(output)
            except Exception as e:
                print("Bulk error:", e)

        elif cmd.startswith("exportjson"):
            parts = cmd.split()
            if len(parts) < 2:
                print("Usage: exportjson <file.json>")
                continue
            try:
                with open(parts[1], "w") as f:
                    json.dump(last_results, f, indent=4)
                print("Exported to JSON.")
            except Exception as e:
                print("Export error:", e)

        else:
            print("Unknown command. Type 'help'.")

if __name__ == "__main__":
    shell()
