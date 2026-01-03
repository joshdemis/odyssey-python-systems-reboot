# main.py
from pathlib import Path
from storage import load_data, save_data
from users import user_exists, rename_user

path = Path("users.json")
data = load_data(path)
users = data["users"]

name = input("Enter name: ").strip()

if user_exists(users, name):
    print("User exists")
else:
    users.append({"name": name, "age": 0, "skills": []})
    save_data(path, data)


