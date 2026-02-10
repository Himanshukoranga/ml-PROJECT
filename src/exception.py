import sys
import os 
from .logger import logging 

# Keeping your function but adding the logging part!
def error_message(message: str) -> None:
    # This is the secret sauce: sending the message to your log file
    logging.error(message) 
    # Still printing to terminal so you can see it live
    print(f"Error: {message}", file=sys.stderr)
    # sys.exit(1) # Commented out so you can test all 4 at once!

# --- 1. FileNotFoundError (Your original one) ---
file_path = "/nonexistent/data.txt"
try:
    with open(file_path, 'r') as f:
        content = f.read()
except FileNotFoundError as e:
    error_details = f"Failed to open file. Type: {type(e).__name__}, Path: {os.path.abspath(file_path)}"
    error_message(error_details)

# --- 2. ZeroDivisionError ---
try:
    result = 10 / 0
except ZeroDivisionError as e:
    error_message(f"Math Error: {e}")

# --- 3. TypeError ---
try:
    bad_sum = "10" + 5
except TypeError as e:
    error_message(f"Type Mismatch: {e}")

# --- 4. IndexError ---
try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError as e:
    error_message(f"List Error: {e}")
