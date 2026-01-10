##namespace

'''
    Python never stores “variables”.
    It stores objects, and names are just labels bound to those objects.        
'''

##LEGB: local, enclosing, global, builtins 

##Error
# x = 10
# def f():
#     x
#     x = x + 1
'''
    Because the presence of assignment makes x local at compile time, not runtime.
Python decides scope before execution, when building bytecode.
'''

##fix
# x = 10
# def f():
#     global x
#     x = x + 1

# def outer():
#     x = 10
#     def inner():
#         nonlocal x  #Without nonlocal, x becomes local to inner and breaks.
#         x += 1
#         return x
#     return inner

# x = "global"

# def outer():
#     x = "enclosing"
#     def inner():
#         nonlocal x
#         x=x.upper()
#         print(x)
#     return inner

# f = outer()
# f()


###Inspecting namespaces

# def f(a,b):
#     c=a+b
#     print(locals())
# f(2,3)

# import builtins
# print(dir(builtins))

###How Python finds modules (sys.path matters)
# import sys 
# print(sys.path)

##Import-time execution pitfalls

##bad 
# print("Loading config...")
# CONFIG = load_from_db()

##good 

# CONFIG = None
# def load():
#     global CONFIG
#     if CONFIG is None:
#         CONFIG = load_from_db()
#     return CONFIG
