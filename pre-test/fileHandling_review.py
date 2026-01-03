# f=open("users.txt")
# print(f.read())
# f.close()

# with open("users.txt") as f:
#     for x in f:
#         print(x)


# with open("demofile.txt", "w") as f:
#   f.write("Now the file has more content!")

# #open and read the file after the appending:
# with open("demofile.txt") as f:
#   print(f.read())

# import os

# file_name = "demo2.txt"

# if os.path.exists(file_name):
#     with open(file_name, 'w') as f:
#         f.write("Content overwritten")
#     print('content overwritten')
# else:
#     print("creating new file...")
#     with open(file_name,'x') as f:
#         f.write('adding content to the new file')
#     print(file_name, 'has been created')


## =================

# with open("data.txt", "r") as f:
#     data = f.read()

  ## most common 
# with open("data.txt", "r") as f:
#     for line in f:
#         print(line.strip())

# with open("data.txt", "a") as f:
#     f.write("hello\n")


# from pathlib import Path

# path = Path("data7.txt")
# if path.exists():
#     path.write_text("hello")  ##same as open("data.txt", "w")
# else:
#     print("File not found")


# from pathlib import Path

# path = Path("data.txt")

# if path.exists():
#     with path.open("a") as f:
#         f.write("hello\n")
# else:
#     print("File not found")

# from pathlib import Path

# path = Path("data.txt")

# if path.exists():
#     content = path.read_text()

#     with path.open("a") as f:
#         if content and not content.endswith("\n"):
#             f.write("\n")
#         f.write("hello\n")
# else:
#     print("File not found")

# import json
# from pathlib import Path

# path = Path("data.json")

# if path.exists():
#     data = json.loads(path.read_text())
#     print(data)
# else:
#     print("File not found")


# import json
# from pathlib import Path

# data = {
#     "name": "Josh",
#     "age": 28,
#     "skills": ["python", "cloud"]
# }

# path = Path("data.json")
# path.write_text(json.dumps(data, indent=2))

# import json
# from pathlib import Path

# path = Path("data.json")

# # 1. Read
# data = json.loads(path.read_text())

# # 2. New user (plain Python dict)
# new_user = {
#     "name": "Linus",
#     "age": 30,
#     "skills": ["linux", "systems"]
# }

# # 3. Modify
# data["users"].append(new_user)

# # 4. Write back
# path.write_text(json.dumps(data, indent=2))


# import json
# from pathlib import Path

# path = Path("users.json")

# # 1. Load existing data
# if path.exists():
#     try:
#         data = json.loads(path.read_text())
#     except json.JSONDecodeError:
#         data = {"users": []}
# else:
#     data = {"users": []}

# users = data["users"]

# # 2. Get input
# name = input("Enter name: ").strip()
# age = int(input("Enter age: ").strip())
# skills_input = input("Enter skills (comma separated): ").strip()

# skills = [s.strip() for s in skills_input.split(",") if s.strip()]

# # 3. Prevent duplicates (by name)
# existing_names = {u["name"].lower() for u in users}

# if name.lower() in existing_names:
#     print("User already exists. Not added.")
# else:
#     new_user = {
#         "name": name,
#         "age": age,
#         "skills": skills
#     }

#     users.append(new_user)
#     path.write_text(json.dumps(data, indent=2))
#     print("User added successfully.")


###Upgraded version of the above logic ==========


# import json 
# from pathlib import Path

# path = Path("users.json")

# if path.exists():
#     try:
#         data = json.loads(path.read_text())
#     except json.JSONDecodeError:
#         data = {"users": []}
# else:
#     data = {"users",[]}

# users = data["users"]

# ##prevent duplicate; key:name 

# existing_names = {u["name"].lower() for u in users}

# while True:
#     name = input("Enter name: ").strip()
#     if not name:
#         print("Name cannot be empty")
#         continue
#     if name.lower() in existing_names:
#         print("Name already exists. Please choose a different name.")
#     else:
#         break

# age = int(input("Enter age: ").strip())

# skills_input = input("Enter skills (comma separated): ").strip()
# skills = [s.strip() for s in skills_input.split(",") if s.strip()]

# new_user = {
#     "name": name,
#     "age": age,
#     "skills": skills
# }

# users.append(new_user)
# path.write_text(json.dumps(data, indent=2))

# print("User added successfully.")


###More Upgraded version of the above logic ==========

# import json
# from pathlib import Path

# path = Path("users.json")

# # Load data safely
# if path.exists():
#     try:
#         data = json.loads(path.read_text())
#     except json.JSONDecodeError:
#         data = {"users": []}
# else:
#     data = {"users": []}

# users = data["users"]

# # Build lookup
# name_map = {u["name"].lower(): u for u in users}

# # Ask for name
# while True:
#     name = input("Enter name: ").strip()
#     if not name:
#         print("Name cannot be empty.")
#         continue

#     lower_name = name.lower()

#     if lower_name in name_map:
#         choice = input(
#             "User exists. Rename this user? (y/n): "
#         ).strip().lower()

#         if choice == "y":
#             new_name = input("Enter new name: ").strip()
#             if not new_name:
#                 print("New name cannot be empty.")
#                 continue

#             name_map[lower_name]["name"] = new_name
#             path.write_text(json.dumps(data, indent=2))
#             print("User renamed successfully.")
#             break
#         else:
#             print("No changes made.")
#             break
#     else:
#         # New user flow
#         age = int(input("Enter age: ").strip())
#         skills_input = input("Enter skills (comma separated): ").strip()
#         skills = [s.strip() for s in skills_input.split(",") if s.strip()]

#         users.append({
#             "name": name,
#             "age": age,
#             "skills": skills
#         })

#         path.write_text(json.dumps(data, indent=2))
#         print("New user added successfully.")
#         break
