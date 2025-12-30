# def greet(name):
#     return f"Hello, {name}! I'm proud of you. You successfully completed the test."
# print(greet("Josh"))


# def addTwoNumbers(a,b):
#     return a+b

# print(addTwoNumbers(6,6))

# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits

# print(x[1],x[4],x[0],z[0],z[1])

# x= 3+5j
# print(x.imag)
# a = "123"
# b = int(a)

# print(type(a))

"""
Comments should explain why, not what.
If the code needs comments to explain what it does, the code is bad.
"""
# print("10"*3)

# a= 3-5j
# b= 6+9j

# print(a*b)


# list = ['apple','banana','cherry']
# list2 = set(list)
# list.append('banana')
# list.append('orange')
# list2.add('orange')
# list2.add('banana')

# list[2]='peach'
# list = list2
# for l in list:
#     print(l)
# print('===========')
# for l2 in list2:
#     print(l2)

# print('list: ', type(list), len(list), list)
# print('list2: ', type(list2), len(list2), list2)



# mylist = ['apple', 'banana', 'cherry']
# mylist[1:2] = ['kiwi', 'mango']
# print(mylist[1:2])

# i=0
# while i<len(mylist):
#     print(mylist[i])
#     i+=1

# fruits = ["apple", "banana", "cherry"]
# newlist = [x for x in fruits if x in ["peach", "orange"]]
# print(newlist)

# fruits.reverse()
# print(fruits)


# discount_rate = 25
# users = ("josh","dan","ment","Diaz")
# users = tuple(name.lower() for name in users)
# raw_user = input("Enter your name: ")
# user = raw_user.strip().lower()

# if user in users:
#     print(f"Congrats {raw_user.strip().capitalize()}, you'll get {discount_rate}% discount!")
# else:
#     print("Sorry, you are not a member!")


# from pathlib import Path
# FILE = Path("users.txt")

# if FILE.exists():
#     users = {line.strip().lower() for line in FILE.read_text().splitlines()}
# else:
#     users = set()
# protected_users = {'josh', 'dan'}
# raw_user = input("Enter user name: ")
# user = raw_user.strip().lower()

# if user in protected_users:
#     print (f"Hi {raw_user.strip().capitalize()}, your account cannot be deleted. Please contact the suport team")
# else:
#     try:
#         users.remove(user)
#         FILE.write_text("\n".join(sorted(users)))
#         print(f"congrats {raw_user.strip().capitalize()} you're now removed from the list")
#     except KeyError:
#         print('User not found')

#=============Dictionary============

# users_info={
#     "name": "Josh",
#     "age":26,
#     "is_active":True
# }
# for key,value in users_info.items():
#     print(key,':', value)


# users = {
#     "josh": {"role": "admin", "active": True},
#     "dan": {"role": "user", "active": False}
# }

# raw_user = input("Enter your username to check your role: ")
# user = raw_user.strip().lower()
# role = users.get(user,{}).get('role')
# if role:
#     print(f"Hi {raw_user.strip().capitalize()}, your role is {users[user]['role']}")
# else:
#     print("You are not yet registered in our system.")
# users = {
#     "josh": {"role": "admin", "active": True},
#     "dan": {"role": "user", "active": False}
# }
# for user, user_info in users.items():
#     print(user)
#     for key, value in user_info.items():
#         print(key, ':',value)

# import json
# from pathlib import Path

# data= json.loads(Path("user_info.json").read_text())
# users = data["users"]
# for user, info in users.items():
#     print(f"{user}: role={info['role']}, active={info['active']}, email={info['email']}")


#==============match============

# import json
# from pathlib import Path

# data= json.loads(Path("user_info.json").read_text())
# users = data["users"]

# raw_user =input("Name: ")
# user = raw_user.strip().lower()
# display_name = raw_user.strip().capitalize()

# if user in users:
#     match users[user]:
#         case{'role': role}:
#             print(f"{display_name.capitalize()} is a(an) {role}")
#         case _:
#             print("User data is invalid")
# else:
#     print("User not found")


#==============functions===========


# def greetings(name, age):
#     return f"Hi {name}, you are {age} years old!"
# message= greetings('John',65)
# print(message)

#===============variable scope=============
# x= 10 # global variable
# def func():
#     x= 9 #enclosing variable 
#     def innerfunc():
#         x=8 #local variable
#         print(x)
#     innerfunc()
#     print(x)
# func()
# print(x)

#=========decorator=========

# def changecase(func):
#     def innerfunc():
#         return func().upper()
#     return innerfunc

# @changecase
# def newfunc():
#     return "hi there"

# print(newfunc())


# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Hello Sally"

# print(myfunction())


# from functools import wraps

# def log_call(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print (f"Calling {func.__name__}")
#         print("args:", args)
#         print("kwargs:", kwargs)
#         result= func(*args, **kwargs)
#         print("return: ", result)
#         return result
#     return wrapper

# @log_call
# def add(a,b):
#     return a+b

# add(4,5)

# from functools import wraps
# import time
# def log_time(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         end = time.perf_counter()
#         duration = end-start
#         print(f"{func.__name__} took {duration:.8f}s")
#         print("resullt: ",result)
#     return wrapper

# @log_time
# def add(a,b):
#     return a+b

# add(4,5)


#=========lambda========= Lambdas are inline helpers, not real functions.

#lambda = arguments: expression 

# x=lambda a,b:a*b
# print(x(4,5))

# def myfunc(n):
#     return lambda a:a+n
# newfunc = myfunc(6)
# print(newfunc(5))

# num = [6,2,3,4,5]
# students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
# # doubled = list(map(lambda x: x*2, num))
# odd = list(filter(lambda x: x%2!=0, num))
# print(f"odd:{odd}")
# even = list(filter(lambda x: x%2==0, num))
# print(f"odd:{even}")
# srt = list(sorted(students, key=lambda x:x[1]))
# print(f"srt:{srt}")


#===========recursion ==========

# def factorial(n):
#     if n==1 or n==0:
#         return 1
#     return n*factorial(n-1)

# print(factorial(5))

# def sum_to_zero(n):
#     if n<0:
#         raise ValueError("number must be positive")
#     if n==0:
#         return 0
#     return n+sum_to_zero(n-1)

# print(sum_to_zero(100))





# data = [1, [2, 3, [1, 4]], 1, [1, [1, 5]]]

# if isinstance(data,list):
#     for i in data:
#         if isinstance(i, int):
#             print(i)
#         else:
#             for j in i:
#                 if isinstance(j,int):
#                     print(j)
#                 else:
#                     for k in j:
#                         print(k)


# def process(data):
#     for element in data:
#         if isinstance(element, list):
#             process(element)
#         else:
#             print(element)
# process(data)

# data = [1, [2, 3, [1, 4]], 1, [1, [1, 5]]]
# def count_occurrences(data, target):
#     total = 0

#     for element in data:
#         if isinstance(element, list):
#             total += count_occurrences(element, target)
#         else:
#             if element == target:
#                 total += 1

#     return total
# print(count_occurrences(data, 1)) 


# data=[10, 20, 30]

# def count_items(data):
#     # base case
#     if data == []:
#         return 0

#     # recursive case
#     return 1 + count_items(data[1:])


# print(count_items(data))

# l2 = [1, 2, 1, 3, 1]

# def count_occurences(data, target):
#     if data == []:
#         return 0
#     return (1 if data[0]==target else 0) + count_occurences(data[1:],target)

# print(count_occurences(l2, 1))



# l2 = [1, 2, 1, 3, 1]

# def count_occurences(data, target):
#     if data ==[]:
#         return 0
#     return (1 if data[0]==target else 0) + count_occurences(data[1:], target)

# print(count_occurences(l2,1))
def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)

l1= list(range(1,8))
for i in l1:
    print(fib(i))