"""Practical file handling examples for students.

This script demonstrates common file operations with safe patterns:
- writing, reading, and appending text files
- simple CSV and JSON read/write
- handling common file-related exceptions

Run this file to create example files in the same folder and see printed output.
"""

from pathlib import Path
import csv
import json


BASE = Path(__file__).parent


def write_text_file(path: Path, content: str):
    """Write text to a file using a context manager (overwrites existing file)."""
    try:
        with path.open("w", encoding="utf-8") as f:
            f.write(content)
        return True
    except PermissionError:
        print("Permission denied when writing to", path)
        return False


def read_text_file(path: Path):
    """Read and return the contents of a text file. Handles FileNotFoundError."""
    try:
        with path.open("r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("File not found:", path)
        return None


def append_lines(path: Path, lines):
    """Append multiple lines to a file (creates file if not exists)."""
    with path.open("a", encoding="utf-8") as f:
        for line in lines:
            f.write(str(line).rstrip("\n") + "\n")


def simple_csv_write(path: Path, rows):
    """Write a small CSV file using the csv module."""
    with path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["name", "age", "email"])
        writer.writerows(rows)


def simple_csv_read(path: Path):
    """Read CSV and return list of dicts.

    Demonstrates using csv.DictReader for structured data.
    """
    results = []
    try:
        with path.open("r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                results.append(row)
    except FileNotFoundError:
        print("CSV file not found:", path)
    return results


def json_write_read(path: Path, data):
    """Write a Python object to JSON and read it back."""
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def main():
    # Prepare example paths
    text_path = BASE / "example_text.txt"
    csv_path = BASE / "example_data.csv"
    json_path = BASE / "example_data.json"

    # 1) Write and read text
    write_text_file(text_path, "Hello\nThis is an example text file.\n")
    print("Read text file contents:\n", read_text_file(text_path))

    # 2) Append lines
    append_lines(text_path, ["Appended line 1", "Appended line 2"])
    print("After append:\n", read_text_file(text_path))

    # 3) CSV example
    rows = [("Alice", 30, "alice@example.com"), ("Bob", 25, "bob@example.com")]
    simple_csv_write(csv_path, rows)
    print("CSV read as dicts:", simple_csv_read(csv_path))

    # 4) JSON example
    data = {"project": "week2_examples", "items": [1, 2, 3]}
    read_back = json_write_read(json_path, data)
    print("JSON read back:", read_back)


if __name__ == "__main__":
    main()
