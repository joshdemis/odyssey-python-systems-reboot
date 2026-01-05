# try:
#     ...
# except SomeError:
#     ...
# else:
#     ...
# finally:
#     ...

 ##Base
# try:
#     risky_operation()
# except SomeError:
#     handle_error()

##else: runs only if no exception occurred.
# try:
#     x = int(input("Enter number: "))
# except ValueError:
#     print("Not a number")
# else:
#     print("You entered:", x)


##finally: (always runs, no exceptions)

# try:
#     f = open("data.txt")
#     data = f.read()
# except FileNotFoundError:
#     print("File missing")
# finally:
#     f.close()


##========Raise/Catch=========

# You raise an exception where the problem happens.
# You catch an exception where you can do something meaningful about it.

# def load_age(value):
#     if value <= 0:
#         raise ValueError ("Age cannot be zero or negative")
#     return value

# value = int(input("Enter your age: "))
# print(load_age(value))

# Catch exceptions at system boundaries.
# Raise exceptions inside business logic.
# try:
#     age = int(input("Enter age: "))
# except ValueError:
#     print("Please enter a valid number.")



# def create_user(name, age):
#     if not name:
#         raise ValueError ("Name required")
#     if age <0:
#         raise ValueError ("Invalid age")
#     return{f"Name: {name}, Age: {age}"}

# try:
#     name = input("Name: ")
#     age = int(input("Age: "))
#     user = create_user(name, age)
# except ValueError as e:
#     print(e)
# else:
#     print(f"User created: {user}")
###=========Custom Exceptions=============
''' Built-in exceptions describe failures.
Custom exceptions explain them.'''

# class UserError(Exception):
#     pass

# def create_user(name, age):
#     if not name:
#         raise UserError("Name is required")
#     if age < 0:
#         raise UserError("Age must be non-negative number")
#     return {"name": name, "age": age}

# # main.py
# try:
#     name = input("Name: ")
#     age = int(input("Age: "))
#     user = create_user(name, age)
# except (ValueError,UserError) as e:
#     print(f"User error: {e}")
# else:
#     print("User created:", user)

###============Exception design for libraries==========

# from pathlib import Path

# class StorageError(Exception):
#     pass

# def load_data(path):
#     if not path.exists():
#         raise StorageError("Data file not found")

# path = Path("data.txt")
# try:
#     data = load_data(path)
# except StorageError as e:
#     print("Cannot start application:", e)


# class StorageError(Exception):
#     pass

# def load_data(path):
#     try:
#         return json.loads(path.read_text())
#     except (OSError, json.JSONDecodeError) as e:
#         raise StorageError("Failed to load data") from e

### =======Error handling with files and JSON==========
class StorageError(Exception):
    pass

import json
from pathlib import Path

def load_data(path):
    if not path.exists():
        raise StorageError("Data file does not exist")
    
    try:
        text =path.read_text()
    except OSError as e:
        raise StorageError("Cannot read data file") from e
    
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        raise StorageError("Invalid JSON format") from e
    
    if "users" not in data or not isinstance(data["users"], list):
        raise StorageError ("Invallid data structure")
    
    return data 

path = Path("users.json")

load_data(path)