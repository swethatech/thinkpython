'''Exercise 15.1. Write a function called distance_between_points that takes two Points as arguments and returns the distance between them.'''


'''def distance_between_points(x,y):
    a=abs(x[0]-y[0])
    b=abs(x[1]-y[1])
    c=(x**2+y**2)**.5
    return c'''




'''Exercise 15.2. Write a function named move_rectangle that takes a Rectangle and two numbers
named dx and dy. It should change the location of the rectangle by adding dx to the x coordinate of
corner and adding dy to the y coordinate of corner.'''


'''def move_rectangle(rect,dx,dy):
    rect.corner.x+=dx
    rect.corner.y+=dy'''







'''Exercise 15.3. Write a version of move_rectangle that creates and returns a new Rectangle
instead of modifying the old one.'''

'''import copy
def move_rectangle(rect,dx,dy):    
    a=copy.deepcopy(rect)
    a.corner.x+=dx
    a.corner.y+=dy
    return a'''
