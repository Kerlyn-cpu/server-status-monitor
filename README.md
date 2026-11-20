# Server Status Monitor

## Description
A simulation of a server status monitoring tool. It reads server states from a JSON database, allows the user to check the status of a specific server, and toggle it between "online" and "offline", saving the updated state back to the file.

## Features
- Reads and parses JSON data.
- Updates JSON dictionaries in memory.
- Writes modified data back to the JSON file with proper indentation.
- Simple CLI interface for checking and updating server states.

## Technologies Used
- Python 3
- `json` module
- `pathlib` module

## How to Run
1. Ensure you have a `servers01.json` file in the same directory.
2. Run the script:
   `python3 monitor01.py`
3. Follow the prompts to check or change a server's status.
