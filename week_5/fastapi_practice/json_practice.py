import json

def read_json_file(file_path):
    """Reads a JSON file and returns the data. Returns [] if file doesn't exist or is invalid."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []   # return empty list if file doesn't exist
    except json.JSONDecodeError:
        return []   # return empty list if file is corrupted


def write_json_file(file_path, new_data):
    """Appends new data to a JSON file. Creates the file if it doesn't exist."""
    
    # Load existing data (or empty list if not exists)
    data = read_json_file(file_path)

    # Ensure data is a list for appending
    if not isinstance(data, list):
        data = [data]

    # Append new data
    data.append(new_data)

    # Save updated data back to file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


write_json_file("data.json", {"name": "Ali", "age": 25})
write_json_file("data.json", {"name": "Sara", "age": 30})

print(read_json_file("data.json"))
