#Exercise 17.1

'''class Time(object):
    def time_to_int(self):
        minutes = time.hour * 60 + time.minute
        seconds = minutes * 60 + time.second
        return seconds

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

print time.time_to_int()'''


#Exercise 17.2

'''class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def print_point(self):
        print "x =", self.x, ",",
        print "y =", self.y

point = Point()
point.print_point()

point = Point(10)
point.print_point()

point = Point(20, 30)
point.print_point()'''


#Exercise 17.3

'''class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)

point = Point()
print point

point = Point(10)
print point

point = Point(10, 15)
print point'''


#Exercise 17.4

'''class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

point1 = Point(1, 3)
point2 = Point(4, 5)

print point1 + point2'''

#Exercise 17.5

'''class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        point_ = Point()
        if isinstance(other, Point):
            point_.x += self.x + other.x
            point_.y += self.y + other.y
            return point_
        elif type(other) == tuple:
            point_.x += self.x + other[0]
            point_.y += self.y + other[1]
        return point_

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

point1 = Point(1, 6)
point2 = (5, 2)
point3 = point1 + point2
point4 = point2 + point1
print point3, point4'''

#Exercise 17.6

'''class Kangaroo(object):
    def __init__(self):
        self.pouch_contents = []

    def put_in_pouch(self, thing):
        self.pouch_contents.append(thing)

    def __str__(self):
        return "I have {} in my pouch".format(self.pouch_contents)

    def __repr__(self):
        return 'Kangaroo <{}>'.format(self.pouch_contents)'''


