# main.py
import argparse
from colorama import Fore, Style, init
from analyzer import analyze_log

# Initialize colorama
init(autoreset=True)

# Map log levels to colors
COLOR_MAP = {
    "INFO": Fore.GREEN,
    "WARNING": Fore.YELLOW,
    "ERROR": Fore.RED
}

def main():
    parser = argparse.ArgumentParser(description="Log Analyzer CLI Tool")
    parser.add_argument("command", help="Command to run (analyze, view, errors)")
    parser.add_argument("file", help="Path to log file")
    args = parser.parse_args()

    if args.command == "analyze":
        result = analyze_log(args.file)
        if result:
            print("\nLog Summary:")
            for key, value in result.items():
                color = COLOR_MAP.get(key, Fore.WHITE)
                print(f"{color}{key}: {value}")

    elif args.command == "view":
        try:
            with open(args.file, "r") as file:
                for line in file:
                    line_stripped = line.strip()
                    printed = False
                    for level in COLOR_MAP:
                        if level in line:
                            color = COLOR_MAP[level]
                            print(f"{color}{line_stripped}")
                            printed = True
                            break
                    if not printed:
                        # Lines without a known log level
                        print(line_stripped)
        except FileNotFoundError:
            print(Fore.RED + "Error: File not found.")

    elif args.command == "errors":
        try:
            with open(args.file, "r") as file:
                for line in file:
                    if "ERROR" in line:
                        print(Fore.RED + line.strip())
        except FileNotFoundError:
            print(Fore.RED + "Error: File not found.")

    else:
        print(Fore.RED + "Unknown command.")

if __name__ == "__main__":
    main()