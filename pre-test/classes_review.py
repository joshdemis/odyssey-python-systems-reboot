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

#========instance methods: “What can this specific object do?”
# class Person:
#     def __init__(self, name):
#         self.name =name 
#     def greet(self):
#         print(f"Hi, I am {self.name}")

# p = Person('Josh')
# p.greet()  #translated to Person.greet(p)


#===========Class methods

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


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def celebrate_birthday(self):
#     self.age += 1
#     return f"Happy birthday! You are now {self.age}"

# p1 = Person("Linus", 25) #age:25
# p2 = Person("Linus", 25) #age:25
# p1.celebrate_birthday() #age:25+1
# # p1.celebrate_birthday() #age would be 25+1+1 if called
# p1.celebrate_birthday() #age: 25+1+1
# print(p1.celebrate_birthday()) #age: 25+1+1+1=28
# print(p2.celebrate_birthday()) #called only once so just +1


# from datetime import date
# class Person:
#     def __init__(self, name, age, birth_month, birth_day):
#         self.name = name
#         self.age = age
#         self.birth_month = birth_month
#         self.birth_day = birth_day
#         self.last_celebrated_year = None

#     def celebrate_birthday_if_today(self):
#         today = date.today()

#         if (today.month == self.birth_month and
#             today.day == self.birth_day and
#             self.last_celebrated_year != today.year):

#             self.age += 1
#             self.last_celebrated_year = today.year
#             print(f"Happy birthday {self.name}! You are now {self.age}")


##============Instance vs class vs static method=========

                ## instance method:

# class Person:
#     def __init__(self, name):
#         self.name=name

#     def greet(self):
#         return f"Hi, I'm {self.name}"

# p1 =Person('Josh')
# print(p1.greet())

                ## class method:

# class Person:
#     species = 'Human'

#     @classmethod
#     def get_species(cls):
#         return cls.species

#   ##usage
# p1 = Person.get_species()


                ## static method:
# class Calculator:
#     @staticmethod
#     def add(a, b):
#         return a + b

   ##Usage 
# Calculator.add(3, 4)


  ##good 
# class UserValidator:
#     @staticmethod
#     def is_valid_email(email):
#         pass

#   ##bad
# def is_valid_email(email):
#     ...

                # Ask, in order: to choose which method to use

                # Does it use instance data?
                # → instance method

                # Does it create or depend on the class itself?
                # → class method

                # Does it use neither but conceptually belong here?
                # → static method

                # Does it belong nowhere in particular?
                # → free function


###__repr__ vs __str__

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

#     def __repr__(self):
#         return f"Person(name={self.name!r}, age={self.age})"

# p = Person("Josh", 28)
# print(p)
# print(repr(p))
# print([p])

###The three correct patterns

##Pattern1
# class User:
#     def __init__(self, name):
#         self.name = name
#         self.tags = []

#   ##Usage
# u1 = User('Josh')
# u1.tags.append('Admin')
# u1.tags.append('Staff')
# print(u1.tags)

##Patern2:
# class User:
#     def __init__(self, name, tags):
#         self.name = name
#         self.tags = tags

# initial_tags = ["admin", "staff"]
# u = User("Josh", initial_tags)
# u.tags.append("active")
# print(initial_tags)   #initial_tags was mutated

##Pattern 3: Tags are optional (safe + flexible, most common)

# class User:
#     def __init__(self, name, tags=None):
#         self.name = name
#         self.tags = tags  if tags is not None else []
# ##Usage 
# initial_tags =['Admin', 'Staff', 'Board']
# u1 = User('Josh',initial_tags)
# u1.tags.append('Active')
# print(u1.tags)


# class Playlist:
#   def __init__(self, name, songs=None):
#     self.name = name
#     self.songs = songs if songs is not None else []

#   def add_song(self, song):
#     self.songs.append(song)
#     print(f"Added: {song}")

#   def remove_song(self, song):
#     if song in self.songs:
#       self.songs.remove(song)
#       print(f"Removed: {song}")

#   def show_songs(self):
#     print(f"Playlist '{self.name}':")
#     for song in self.songs:
#       print(f"- {song}")

# initial_songs_list =['S1', 'S2']
# my_playlist = Playlist("Favorites", initial_songs_list)
# my_playlist.add_song("Bohemian Rhapsody")
# my_playlist.add_song("Stairway to Heaven")
# my_playlist.show_songs()

# print(initial_songs_list)  #['S1', 'S2', 'Bohemian Rhapsody', 'Stairway to Heaven']


## mutable vs immutable

        # How to decide: mutable or immutable?

        # Ask these questions:
        # Does this object represent state that changes over time?
        # → mutable
        # Does this object represent a fact or value?
        # → immutable
        # Will this object be shared across boundaries?
        # → immutable preferred
        # Is performance critical and scope controlled?
        # → mutable acceptable

# ##Mutable 
#  #ex: list, dict, set

# lst = [1, 2]
# lst.append(3)   # same object, changed

# ##Immutable 
#   #ex: int, float, str, tuple, frozenset
# s = "hi"
# s += "!"   # new object created


# from dataclasses import dataclass

# @dataclass(frozen=True)
# class User:
#     name: str
#     age: int

# u1 =User('Josh', 28)

# print(u1.age)


##==============inheritance===========

# class Person:
#     def __init__(self,name):
#         self.name = name 
    
#     def greet(self):
#         return f"Hi, I'm {self.name}"

# class Employee(Person):
#     def __init__(self, name, employee_id):
#         super().__init__(name)
#         self.employee_id = employee_id
#     def user_info(self):
#         return f"{self.name} : {self.employee_id}"

# e1=Employee("Josh", 'S1005')

# print(e1.user_info())
# print(e1.greet())
# print(f"{e1.name}: {e1.employee_id}")


##==================polymorphism===============
# class Animal:
#     def speak(self):
#         raise NotImplementedError

# class Dog(Animal):
#     def speak(self):
#         return "woof"

# class Cat(Animal):
#     def speak(self):
#         return "meow"

# animals = [Dog(), Cat()]
# for a in animals:
#     print(a.speak())
##=========================
# class FileLogger:
#     def write(self, message):
#         print(f"File: {message}")

# class SocketLogger:
#     def write(self, message):
#         print(f"Socket: {message}")

# def log(writer):
#     writer.write("hello")

# log(FileLogger())
# log(SocketLogger())


