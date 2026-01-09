'''
I am stating a fact that must be true here.
If it is not, stop the program immediately.
'''

# discription = "numbers must not be empty"
# def average(num):
#     assert len(num) >0,discription
#     return sum(num)/len(num)
# num = [] #[3,5,8,9]
# print(average(num))

###Assertions can be turned off
# python -O script.py

##===Sanity checks (practical use)

# assert isinstance(data, dict)
# assert "users" in data
# assert isinstance(data["users"], list)

'''
Assertions document assumptions and kill bugs early.
They are not a substitute for error handling.
'''

# def square(x):
#     return x*x

# def test_square():
#     assert square(3) == 8

# user = {'name':'Josh', 'age': 27}
# assert isinstance(user, dict)
# assert 'age' in user