##=========Python Classes/Objects======
# class MyClass:
#   x = "Hello there!"

# obj = MyClass()
# print(obj.x)

# class Person:
#     def __init__(self, name, age, city, country):
#         self.name = name 
#         self.age = age 
#         self.city = city
#         self.country = country

#     def describe(self):
#         return f"{self.name} is {self.age} years old. Lives in {self.city}, {self.country}"

# p1 = Person('Josh', 34, 'NY', 'USA')
# print(p1.describe())



# class Person:
#   def __init__(self, name):
#     self.name = name

#   def greet(self):
#     return "Hello, " + self.name

#   def welcome(self):
#     message = self.greet()
#     return message + "! Welcome to our website."
  
#   def final_message(self):
#     fm=self.welcome()
#     print('Final message:', fm)

# p1 = Person("Josh")
# p1.final_message()



# class Calculator:
#     def __init__(self):   #optional, because python will add it anyway
#         pass
#     def add(self, a,b):
#         return a+b
    
#     def multiply(self,a,b):
#         return a*b
    
# calc=Calculator()

# print(calc.add(4,6))
# print(calc.multiply(4,6))

##=========Instance methods vs Class methods===========

#instance methods: “What can this specific object do?”
# class Person:
#     def __init__(self, name):
#         self.name =name 
#     def greet(self):
#         print(f"Hi, I am {self.name}")

# p = Person('Josh')
# p.greet()  #translated to Person.greet(p)


#Class methods

# class Person:
#     species = "Human"

#     @classmethod
#     def get_species(cls):
#         return cls.species
    
# p = Person()
# print(p.get_species())


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_string(cls, s):
#         name, age = s.split(",")
#         return cls(name, int(age))

# p=Person.from_string("Josh,29")
# print(p.name)
# print(p.age)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

# p1=Person('Josh',28)
# print(p1)