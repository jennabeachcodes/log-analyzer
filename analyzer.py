def analyze_log(file_path):
    print("Opening file:", file_path)  # DEBUG LINE

    counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    try:
        with open(file_path, "r") as file:
            for line in file:
                print("LINE:", line.strip())  # DEBUG
                for level in counts:
                    if level in line:
                        counts[level] += 1

        return counts

    except FileNotFoundError:
        print("Error: File not found.")
        return None