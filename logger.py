import os
from datetime import datetime

LOG_FILE = "logs/chat_logs.txt"


def log_interaction(user_input, agent_response):
    """
    Stores conversation logs.
    """

    os.makedirs("logs", exist_ok=True)

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write("=" * 60 + "\n")
        file.write(f"Timestamp : {datetime.now()}\n")
        file.write(f"User      : {user_input}\n")
        file.write(f"Agent     : {agent_response}\n")
        file.write("=" * 60 + "\n\n")


def log_error(error):
    """
    Stores runtime errors.
    """

    os.makedirs("logs", exist_ok=True)

    with open("logs/error_logs.txt", "a", encoding="utf-8") as file:
        file.write(f"[{datetime.now()}] {error}\n")