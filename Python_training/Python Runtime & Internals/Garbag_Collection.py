'''CPython’s primary memory management is reference counting, not “GC magic”.
Every object keeps a counter:
how many references point to me?
When the count hits zero, the object is immediately destroyed.'''

##example:
# a = [1, 2, 3]   # refcount = 1
# b = a           # refcount = 2
# del a           # refcount = 1
# del b           # refcount = 0 → object freed immediately
'''Reference counting breaks when objects reference each other.'''

# class Node:
#     def __init__(self):
#         self.other = None

# a = Node()
# b = Node()

# a.other = b
# b.other = a


'''
a references b
b references a
Even if you delete both names, the objects still reference each other
Refcount never hits zero
'''

'''
--->To fix that, CPython also runs a cycle detector.
'''

# import gc
# gc.collect()

''''You don’t normally control this manually. It runs automatically.'''

###Inspecting garbage collection

# import gc

# print(gc.get_count())
# print(gc.get_threshold())

# gc.set_debug(gc.DEBUG_LEAK)

# gc.collect()
# print(gc.garbage)

