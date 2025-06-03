import json
import os
from datetime import datetime, timedelta

DB_PATH = "database.json"

def load_db():
    if not os.path.exists(DB_PATH):
        return {}
    with open(DB_PATH, "r") as f:
        return json.load(f)

def save_db(data):
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=2)

def is_premium(user_id):
    db = load_db()
    expiry_str = db.get(str(user_id))
    if not expiry_str:
        return False
    expiry = datetime.strptime(expiry_str, "%Y-%m-%d")
    return expiry >= datetime.today()

def get_expiry_date(user_id):
    db = load_db()
    expiry_str = db.get(str(user_id))
    if not expiry_str:
        return None
    return datetime.strptime(expiry_str, "%Y-%m-%d")

def get_days_remaining(user_id):
    expiry = get_expiry_date(user_id)
    if not expiry:
        return 0
    remaining = (expiry - datetime.today()).days
    return max(remaining, 0)

def add_premium(user_id, days):
    db = load_db()
    today = datetime.today()
    expiry = today + timedelta(days=days)
    db[str(user_id)] = expiry.strftime("%Y-%m-%d")
    save_db(db)
    return expiry.strftime("%Y-%m-%d")
