# a = [1, 2, 3]
# b = a

'''
    a ──▶ [1, 2, 3]
    b ──▶ same object

'''

# b.append(4)
# print(a)  # [1, 2, 3, 4]


# def f(x):
#     x.append(99)

# lst = [1, 2, 3]
# f(lst)
# print(lst)  # [1, 2, 3, 99]


# def f(x):
#     x = [9, 9, 9]
#     return x

# lst = [1, 2, 3]
# print(f(lst))  #[9, 9, 9]
# print(lst)  # [1, 2, 3]

'''
    Rebinding x does not affect lst
    Only mutation affects shared objects
'''
###Immutable objects (int, str, tuple, frozenset):

# def f(x):
#     x += 1
#     return x

# a = 10
# print(f(a))
# print(a)  # 10, Because x += 1 creates a new integer object and rebinds x


##Mutable objects (list, dict, set):
# def f(x):
#     x.append(1)

# lst = []
# f(lst)
# print(lst)  # [1]


###Shallow copy vs deep copy

# import copy

# a = [[1, 2], [3, 4]]

# b = a            # alias
# c = a.copy()     # shallow copy
# d = copy.deepcopy(a)  # deep copy

''''
    Memory picture:
    a and b share everything
    c is a new outer list, but inner lists are shared
    d is fully independent
'''

##Test it:
# a[0].append(99)

# print(a)  # [[1, 2, 99], [3, 4]]
# print(b)  # same
# print(c)  # same (shallow copy still shares inner lists)
# print(d)  # unchanged


##bad:

# def add_item(x, lst=[]):
#     lst.append(x)
#     return lst

# add_item(1)  # [1]
# add_item(2)  # [1, 2]
# add_item(3)  # [1, 2, 3]

'''
    Default arguments are evaluated once at function definition time
    That list is shared across all calls
'''


##god:
# def add_item(x, lst=None):
#     if lst is None:
#         lst = []
#     lst.append(x)
#     return lst


# print(add_item(1))
# print(add_item(2))
# print(add_item(3))



####Reference semantics in real systems

# def normalize(data):
#     for row in data:
#         row["value"] /= 100
#     return data

# train = load_data()
# test = train[:100]  # shallow slice, still same inner dicts

# normalize(train)
# # test is now silently corrupted
