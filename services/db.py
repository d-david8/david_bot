# services/db.py
import json
import os
import logging

USERS_FILE = "users.json"

# Create the users file if it doesn't exist
if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, "w") as f:
        json.dump([], f)

# Function to add a user to the JSON file
def add_user(telegram_id, username, first_name, last_name, language_code=None):
    try:
        # Load existing users
        with open(USERS_FILE, "r") as f:
            users = json.load(f)

        # Check if user already exists
        if any(user["telegram_id"] == telegram_id for user in users):
            logging.warning(f"User {telegram_id} already registered")
            return "already_registered"

        # Add new user
        users.append({
            "telegram_id": telegram_id,
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "language_code": language_code
        })

        # Save back to the file
        with open(USERS_FILE, "w") as f:
            json.dump(users, f, indent=4)
        logging.info(f"User {telegram_id} registered successfully") 
        return "registered_successfully"
    except Exception as e:
        logging.error(f"Error adding user: {e}")
        return "error_adding_user"

# Function to get all users from the JSON file
def get_all_users():
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Error loading users: {e}")
        return []

# Function to find a user by telegram_id
def find_user(telegram_id):
    users = get_all_users()
    for user in users:
        if user["telegram_id"] == telegram_id:
            return user
    logging.warning(f"User {telegram_id} not found")
    return None

# Function to remove a user by telegram_id
def remove_user(telegram_id):
    try:
        with open(USERS_FILE, "r") as f:
            users = json.load(f)

        if not any(user["telegram_id"] == telegram_id for user in users):
            logging.warning(f"User {telegram_id} not found for removal")
            return "not_registered"

        users = [u for u in users if u["telegram_id"] != telegram_id]

        with open(USERS_FILE, "w") as f:
            json.dump(users, f, indent=4)

        logging.warning(f"User {telegram_id} removed successfully")
        return "unregistered_successfully"

    except Exception as e:
        logging.error(f"Error removing user {telegram_id}: {e}")
        return "error"
