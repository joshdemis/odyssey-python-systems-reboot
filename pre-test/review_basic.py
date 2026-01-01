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


# def fib(n):
#     if n<=1:
#         return n
#     return fib(n-1) + fib(n-2)

# l1= list(range(1,8))
# for i in l1:
#     print(fib(i))

##Find the maximum value in a list:

# def find_max(numbers):
#     if len(numbers)==1:
#         return numbers[0]
#     else:
#         max_of_rest =find_max(numbers[1:])
#         return numbers[0] if numbers[0] > max_of_rest else max_of_rest

# my_list = [3, 7, 2, 9, 1]
# print(find_max(my_list))

# def find_max(numbers):
#     current_max = numbers[0]
#     for n in numbers[1:]:
#         if n > current_max:
#             current_max = n
#     return current_max


# def find_max(numbers, index=0):
#     if index == len(numbers) - 1:
#         return numbers[index]

#     max_of_rest = find_max(numbers, index + 1)
#     return numbers[index] if numbers[index] > max_of_rest else max_of_rest


#===========generators===========

# def count_up(n):
#     i = 1
#     while i < n:
#         yield i
#         i += 1

# for item in count_up(8):
#     print(item)


# def read_data():
#     for row in source:
#         yield row

# def clean_data(rows):
#     for r in rows:
#         yield clean(r)

# def train(rows):
#     for r in rows:
#         model.learn(r)

# squares = list((i * i for i in range(8)))
# print(squares)

# def squares(n):
#     for i in range(n):
#         yield i * i
# for item in squares(8):
#     print(item)


# def simple_gen():
#   yield "Emil"
#   yield "Tobias"
#   yield "Linus"

# gen = simple_gen()
# print(next(gen))
# print(next(gen))
# print(next(gen))



# def large_sequence(n):
#   for i in range(n):
#     yield i

# # This doesn't create a million numbers in memory
# gen = large_sequence(1000000)
# print(next(gen))
# print(next(gen))
# print(next(gen))



# list_comp = [x * x for x in range(5)]
# sumnum=0
# for i in list_comp:
#     sumnum +=i

# print(sumnum)
# print(sum(list_comp))

# list_comp = (x * x for x in range(9))   #generator

# print(next(list_comp))
# print(next(list_comp))
# print(next(list_comp))
# list_comp.close()
# print(next(list_comp))



# def gen():
#     try:
#         while True:
#             yield "running"
#     finally:
#         print("cleaning up")

# g = gen()
# next(g)
# next(g)
# g.close()



#========Range==============
##range(start, stop, step)


# r1 = range(1,9,2)
# for i in r1:
#     print(i)
# print(6 in r1)


#===============Python Iterators==========
# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     if self.a >5:
#         raise StopIteration
#     x = self.a
#     self.a += 1
#     return x

# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter)) #raises StopIteration

##==========Modules=============
# import mymodule
# from mymodule import person1

# mymodule.greeting('Josh')
# user_info = person1.items()

# for key,value in user_info:
#     print(key.capitalize(), ':', value)

# import platform

# x = platform.system()
# y=dir(platform)
# print(x)
# print(y)


##==========math============

# import math

# print(math.ceil(math.sqrt(48)))
# print(math.floor(math.pi))


#==========JSON=========

import json

# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)  # the result is a Python dictionary: json to python
# z= json.dumps(y)   #back to json: json to python
# print(type(x)) #json
# print(type(y))  #python
# print(type(z))  #json


##Convert Python objects into JSON strings, and print the values:

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# print(json.dumps(x, indent=3, separators=('.', ' = ')))

##=============RegEx=============
# import re

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)

# print(x)

##=============PIP=========
# pip3 install camelcase

# from camelcase import CamelCase

# print(CamelCase().hump('hello there'))

##========Try Except==========
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.


# try:
#   print(x)
# except NameError:
#   print('x is not defined')
# except:
#   print("An exception occurred")

# try:
#  print(y)
# except:
#  print('Something went wrong')
# else:
#  print('nothing went wrong')
# finally:
#  print('all done')


# try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")

# x = -1

# if x < 0:
#   raise Exception("Sorry, no numbers below zero")


##===========User Input=======

# name = input("Enter your name: ")
# # print(f"Hello {name.stip().capitalize()}!")


# y = True
# while y == True:
#   x = input("Enter a number:")
#   try:
#     x = float(x);
#     y = False
#   except:
#     print("Wrong input, please try again.")

# print("Thank you!")
