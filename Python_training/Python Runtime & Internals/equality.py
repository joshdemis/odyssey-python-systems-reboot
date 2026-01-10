# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
# p1 = Point(1, 2)
# p2 = Point(1, 2)

# p1 == p2  # True
# p1 is p2  # False


# a = 256
# b = 256
# a is b  # True

# a = 257
# b = 257
# a is b  # Often False in CPython. integers are created at runtime


# a = int("257")
# b = int("257")
# print(a is b)
# def f():
#     a = 257
#     b = 257
#     return a is b

# print(f())

# a = 10**3
# b = 10**3
# print(a is b)  # False much more often

# import sys
# print(sys.implementation.name)
# print(sys.version)

# a= 645
# b=645
# print(a is b) #true, Because CPython reused the same integer object for both names.


# x= "word"
# y= "word"

# print(x is y) #true, 

# u=[1,2,3]
# v=[1,2,3]
# print(u is v)  #false, Every list literal like [1,2,3] creates a brand new object.So Python never interns mutable containers.

# x = "".join(["wo", "rd"])
# y = "word"
# print(x is y)  # False, Same value, different object. No interning.
