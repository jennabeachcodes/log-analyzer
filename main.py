import argparse
from analyzer import analyze_log


def main():
    parser = argparse.ArgumentParser(description="Log Analyzer CLI Tool")

    parser.add_argument("command", choices=["analyze", "errors"], help="Command to run")
    parser.add_argument("file", help="Path to the log file (e.g., sample.log)")


    args = parser.parse_args()

    if args.command == "analyze":
        result = analyze_log(args.file)

        if result is not None:
            print("\nLog Summary:")
            for key, value in result.items():
                print(f"{key}: {value}")

    elif args.command == "errors":
        try:
            with open(args.file, "r") as file:
                print("\nError Logs:")
                for line in file:
                    if "ERROR" in line:
                        print(line.strip())
        except FileNotFoundError:
            print("Error: File not found.")


if __name__ == "__main__":
    main()