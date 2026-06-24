import os
import logging
from datetime import datetime

os.makedirs("logs", exist_ok=True)

LOG_FILE="logs/app.log"

def write_log(message):
    with open(LOG_FILE, "a" , encoding="utf-8") as file:
        timestamp=datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
        file.write(f"{timestamp} - {message}\n")


logging.basicConfig(
    filename="logs/error.log",
    level=logging.ERROR,
    format="\nDate & Time: %(asctime)s\nFile Name: %(filename)s\nFunction: %(funcName)s\nLine Number: %(lineno)d\nError Type: %(levelname)s\nMessage: %(message)s\n" + "-" * 70
)