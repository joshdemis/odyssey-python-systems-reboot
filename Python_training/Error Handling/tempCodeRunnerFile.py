class UserError(Exception):
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