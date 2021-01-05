#length (chapter-3)

'''def right_justify(s):
    s=len("allen")
    print(s)
right_justify('allen')'''




# 1. Type this example into a script and test it.

'''def do_twice(f):
   f()
   f()

def print_spam():
   print('spam')

do_twice(print_spam)'''

# 2. Modify do_twice so that it takes two arguments, a function object and
# a value, and calls the function twice, passing the value as an argument.

'''character = input('What word to repeat?\n')

def do_twice(f, character):
   f(character)
   f(character)

def print_spam(character):
   print(character)

do_twice(print_spam,character)'''

# 3. Write a more general version of print_spam, called print_twice, that
# takes a string as a parameter and prints it twice.

'''string = "swetha"

def print_twice(string):
   print(string)
   print(string)

print_twice(string)'''


# 4. Use the modified version of do_twice to call print_twice twice, passing
# 'spam' as an argument.

'''new="spam"
def do_twice(f,new):
   f(new)
   f(new)

def print_spam(new):
   print(new)

do_twice(print_spam,new)'''

# 5. Define a new function called do_four that takes a function object and
# a value and calls the function four times, passing the value as a parameter.
# There should be only two statements in the body of this function, not four.
# You can see my solution at thinkpython.com/code/do_four.py.


'''def do_twice(f, arg):
    f(arg)
    f(arg)

def print_twice(arg):
    print(arg)
    print(arg)

do_twice(print_twice, 'spam')
print('')

def do_four(f, arg):
    do_twice(f, arg)
    do_twice(f, arg)

do_four(print_twice, 'spam')
print('')'''



#This exercise can be done using only the statements and other features we have learned
#so far


'''def do_Func(f,val,iter):
    i=0
    while i<iter:
        f(val)
        i=i+1

def printer(val):
    print(val)

# Create Grid

colCell = '+ - - - - + - - - - +'
rowCell = '|         |         |'

do_Func(printer, colCell, 1)
do_Func(printer, rowCell, 4)
do_Func(printer, colCell, 1)
do_Func(printer, rowCell, 4)
do_Func(printer, colCell, 1)'''



#2. Write a function that draws a similar grid with four rows and four columns

'''x =' + '
y =' -'
w = ' '
z =' | '

f = (x + 4*y + w)*4+x
g = (z + 9* w)*4+z

def print_twice (banana):
    print(banana)
    print(banana)

def do_twice (f, apple):
    f(apple)
    f(apple)

def box ():
    print(f)
    do_twice(print_twice,g)
    print(f)
    do_twice(print_twice,g)

def big_box():
    box()
    box()
    print(f)

big_box()'''