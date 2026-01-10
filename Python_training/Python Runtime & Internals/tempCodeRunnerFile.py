a= 645
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
