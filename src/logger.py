import logging 
import os 
import sys
from datetime import datetime

# --- 1. Logging Setup ---

# Creates a unique, time-stamped log file name 
LOG_FILE = f"{datetime.now().strftime('%d/%m/%Y @ %H_%M_%S')}.log"
# Constructs the full path (e.g., CWD/logs/09_11_2025_XX_XX.log)
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Ensures the 'logs' directory is created 
os.makedirs(os.path.dirname(logs_path), exist_ok=True) 

# Sets the complete path for the configuration
LOG_FILE_PATH = logs_path

# Configures the root logger
logging.basicConfig( 
    filename=LOG_FILE_PATH,
    # Added module name, function name, and line number for robust debugging
    format='[%(asctime)s] %(name)s %(levelname)s [%(funcName)s:%(lineno)d] - %(message)s', 
    level=logging.INFO, 
)

# Optional: Add a StreamHandler to see INFO messages in the console as well
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))
logging.getLogger().addHandler(console_handler)


# --- 2. Verification Function ---

def check_logger_status():
    """Logs test messages and verifies their existence in the created file."""
    
    # Log test messages
    logging.info("LOGGER TEST: The logging system has been initialized successfully.")
    logging.warning("LOGGER TEST: This is a warning message.")
    
    try:
        # Read the file to confirm the content
        with open(LOG_FILE_PATH, 'r') as f:
            content = f.read()
        
        # Check if the initial INFO message is in the content
        if "LOGGER TEST: The logging system has been initialized successfully." in content:
            print("\n" + "="*50)
            print("✅ Logger Verification SUCCESSFUL.")
            print(f"File created and messages logged at: {LOG_FILE_PATH}")
            print(f"Log messages seen in console (StreamHandler active).")
            print("="*50)
        else:
            print("❌ Verification FAILED: Test messages NOT found in the log file.")
            
    except FileNotFoundError:
        print(f"❌ Verification FAILED: Log file not found at {LOG_FILE_PATH}")
    except Exception as e:
        print(f"❌ Verification FAILED: An error occurred while reading the log file: {e}")


if __name__ == "__main__":
    check_logger_status()
    
