#Exercise 5.3.
#Fermat’s Last Theorem says that there are no positive integers a, b, and c such
#that:


'''def check_fermat(a, b, c, n):
    if n > 2 and a ** n + b ** n == c ** n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")


def prompting():
    a = input("Type your value of a: ")
    b = input("Type your value of b: ")
    c = input("Type your value of c: ")
    n = input("Type your value of n: ")

    check_fermat(int(a), int(b), int(c), int(n))


prompting()'''










#Exercise 5.4.
#If you are given three sticks, you may or may not be able to arrange them in
#a triangle. For example, if one of the sticks is 12 inches long and the other
#two are one inch long, you will not be able to get the short sticks to meet in
#the middle.  For any three lengths, there is a simple test to see if it is
#possible to form a triangle:


'''def is_triangle(a, b, c):
    if a > b + c:
        print("No")
    elif b > a + c:
        print("No")
    elif c > a + b:
        print("No")
    else:
        print("Yes")


def prompting():
    a = input("Type length of side a: ")
    b = input("Type length of side b: ")
    c = input("Type length of side c: ")

    is_triangle(int(a), int(b), int(c))


prompting()'''





#Exercise 5.5.
#Read the following function and see if you can figure out what it does. Then run
#it (see the examples in Chapter 4).


'''import turtle
bob = turtle.Turtle()

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

# Draws symetrical lightning-shaped figure with t(urtle) then goes at the starting point?

draw(bob, 20, 5)
turtle.mainloop()'''



#Exercise 5.6.
#The Koch curve is a fractal that looks something like Figure 5.2. To draw a Koch
#curve with length x, all you have to do is


'''import turtle
bob = turtle.Turtle()

def koch(turtle, length):
    if length < 3:
        turtle.fd(length)
        return
    koch(turtle, length/3)
    turtle.lt(60)
    koch(turtle, length/3)
    turtle.rt(120)
    koch(turtle, length/3)
    turtle.lt(60)
    koch(turtle, length/3)

def snowflake(turtle, length):
    for i in range(3):
        koch(turtle, length)
        turtle.rt(120)

koch(bob, 30)

bob.pu()
bob.fd(50)
bob.pd()

snowflake(bob, 30)

turtle.mainloop()'''























