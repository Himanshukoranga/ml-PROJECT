import sys
import os # Import os for path manipulation (optional)

# The function definition (as before)
def error_message(message: str) -> None:
    print(f"Error: {message}", file=sys.stderr)
    sys.exit(1)

# Example usage capturing a FileNotFoundError
file_path = "/nonexistent/data.txt"
try:
    with open(file_path, 'r') as f:
        content = f.read()
except FileNotFoundError as e:
    # Pass the specific details to the error_message function
    error_details = f"Failed to open file. Type: {type(e).__name__}, Path: {os.path.abspath(file_path)}"
    error_message(error_details)