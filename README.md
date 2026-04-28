# Log Analyzer CLI Tool

A command-line tool for parsing and visualizing log files. Quickly summarize log levels, view colorized output, or filter for errors — all from the terminal.

---

## Features

- **Analyze** — counts the total number of `INFO`, `WARNING`, and `ERROR` entries in a log file
- **View** — prints the full log file with color-coded lines by log level
- **Errors** — filters and displays only `ERROR` lines

Output is color-coded using [colorama](https://pypi.org/project/colorama/):

| Log Level | Color |
|---|---|
| `INFO` | Green |
| `WARNING` | Yellow |
| `ERROR` | Red |

---

## Requirements

- Python 3.6+
- [colorama](https://pypi.org/project/colorama/)

Install the dependency with:

```bash
pip install colorama
```

---

## File Structure

| File | Purpose |
|---|---|
| `main.py` | CLI entry point — parses arguments and runs commands |
| `analyzer.py` | Core logic — reads a log file and counts log level occurrences |

---

## Usage

```bash
python main.py <command> <file>
```

### Commands

#### `analyze`
Counts and displays a summary of each log level found in the file.

```bash
python main.py analyze path/to/logfile.log
```

**Example output:**
```
Log Summary:
INFO: 42
WARNING: 7
ERROR: 3
```

#### `view`
Prints the entire log file with each line color-coded by its log level. Lines with no recognized level are printed in the default terminal color.

```bash
python main.py view path/to/logfile.log
```

#### `errors`
Filters the log file and prints only lines containing `ERROR`.

```bash
python main.py errors path/to/logfile.log
```

---

## Expected Log Format

The tool detects log levels by scanning each line for the keywords `INFO`, `WARNING`, or `ERROR`. It is compatible with common log formats such as:

```
2024-01-15 10:23:01 INFO Application started
2024-01-15 10:23:45 WARNING Disk usage above 80%
2024-01-15 10:24:12 ERROR Failed to connect to database
```

No specific format is enforced — any line containing one of the three keywords will be recognized.

---

## Notes

- `analyzer.py` contains debug `print` statements that log the file path and each line as it is read. These can be removed for production use.
- If the specified file does not exist, all commands will print an error message and exit gracefully.
