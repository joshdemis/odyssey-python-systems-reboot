'''Read the error. Slowly. Completely'''    

##1   Read stack traces bottom-up

'''
Traceback (most recent call last):
  File "main.py", line 10, in <module>
    run()
  File "main.py", line 6, in run
    process(data)
  File "users.py", line 12, in process
    age = int(user["age"])
ValueError: invalid literal for int() with base 10: 'abc'
'''


'''
        How to read this correctly:

        Bottom line → what failed
        ValueError: invalid literal for int()

        Line above → where it failed
        users.py, line 12

        Above that → who called it

        Keep going until you reach your code

        Do not start at the top. That’s how people get lost.
'''

##2  Print debugging (allowed, but disciplined)

##3  Use assert as a debugging scalpel
# assert isinstance(user, dict)
# assert "age" in user
# assert isinstance(user["age"], int)


##4 === Step-by-step debugging (pdb)

# import pdb

# pdb.set_trace()

'''
        Useful commands:
        n → next line
        s → step into function
        p variable → print variable
        l → list code
        c → continue
'''
print('Before')
breakpoint()

print("after first bearkpoint")

print("after second breakpoint")