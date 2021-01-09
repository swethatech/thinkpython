#Exercise 16.1. Write a function called print_time that takes a Time object and prints it in the
#form hour:minute:second. Hint: the format sequence '%.2d' prints an integer using at least
#two digits, including a leading zero if necessary.


'''class Time(object):
    """ represents the time of day.
    attributes: hour, minute, second"""

time = Time()
time.hour = 11
time.minute = 59
time.second = 30


def print_time(time):
    print("%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second))

print_time(time)'''


#Exercise 16.2. Write a boolean function called is_after that takes two Time objects, t1 and t2,
#and returns True if t1 follows t2 chronologically and False otherwise. Challenge: don’t use an if
#statement.


'''import time
import datetime


class Time(object):
    """Time object based on datetime.datetime describes time in 24hr format"""

    def __init__(self, year=2000, month=1, day=1, hour=12, minute=0, sec=0):
        self.date = datetime.datetime(year, month, day, hour, minute, sec)

    def mktime(self):
        return time.mktime(self.date.timetuple())


t1 = Time(2013, 1, 3, 15)
t2 = Time(2013, 1, 3, 1)


def is_after(time1, time2):
    return time1.mktime() > time2.mktime()


print(is_after(t1, t2))'''




#Exercise 16.3. Write a correct version of increment that doesn’t contain any loops.
#Anything that can be done with modifiers can also be done with pure functions. In fact,
#some programming languages only allow pure functions. There is some evidence that
#programs that use pure functions are faster to develop and less error-prone than programs
#that use modifiers. But modifiers are convenient at times, and functional programs tend to
#be less efficient.
#In general, I recommend that you write pure functions whenever it is reasonable and resort
#to modifiers only if there is a compelling advantage. This approach might be called a
#functional programming style

'''class Time(object):
    """ represents the time of day.
    attributes: hour, minute, second"""

time = Time()
time.hour = 11
time.minute = 59
time.second = 30


def increment(time, seconds):
    print ("Original time was: %.2d:%.2d:%.2d" % (time.hour, time.minute, time.second))

    time.second += seconds
    if time.second > 59:
        quotient, remainder = divmod(time.second, 60)
        time.minute += quotient
        time.second = remainder
    if time.minute > 59:
        quotient, remainder = divmod(time.minute, 60)
        time.hour += quotient
        time.minute = remainder
    if time.hour > 12:
        time.hour -= 12

    print("Plus %g seconds" % (seconds))
    print("New time is: %.2d:%.2d:%.2d" % (time.hour, time.minute, time.second))

increment(time, 300)'''





#Exercise 16.4. Write a “pure” version of increment that creates and returns a new Time object
#rather than modifying the parameter.

'''import copy


class Time(object):
    """ represents the time of day.
    attributes: hour, minute, second"""

time = Time()
time.hour = 11
time.minute = 59
time.second = 30


def increment(time, seconds):
    print ("Original time was: %.2d:%.2d:%.2d"
          % (time.hour, time.minute, time.second))

    new_time = copy.deepcopy(time)
    new_time.second += seconds
    if new_time.second > 59:
        quotient, remainder = divmod(new_time.second, 60)
        new_time.minute += quotient
        new_time.second = remainder
    if new_time.minute > 59:
        quotient, remainder = divmod(new_time.minute, 60)
        new_time.hour += quotient
        new_time.minute = remainder
    if new_time.hour > 12:
        new_time.hour -= 12

    print("Plus %g seconds" % (seconds))
    print ("New time is: %.2d:%.2d:%.2d"
          % (new_time.hour, new_time.minute, new_time.second))
    print ("memory id of object 'time': ", id(time))
    print ("memory id of object 'new_time': ", id(new_time))

increment(time, 300)'''







#Exercise 16.5. Rewrite increment using time_to_int and int_to_time.
#In some ways, converting from base 60 to base 10 and back is harder than just dealing with
#times. Base conversion is more abstract; our intuition for dealing with time values is better.
#But if we have the insight to treat times as base 60 numbers and make the investment of
#writing the conversion functions (time_to_int and int_to_time), we get a program that
#is shorter, easier to read and debug, and more reliable.

'''import copy


class Time(object):
    """ represents the time of day.
    attributes: hour, minute, second"""

time = Time()
time.hour = 11
time.minute = 59
time.second = 30


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    new_time = Time()
    minutes, new_time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def increment(time, seconds):
    new_time = copy.deepcopy(time)
    new_time = time_to_int(new_time) + seconds
    new_time = int_to_time(new_time)
    print ("New time is: %.2d:%.2d:%.2d"
          % (new_time.hour, new_time.minute, new_time.second))

increment(time, 300)'''




#Exercise 16.6. Write a function called mul_time that takes a Time object and a number and returns
#a new Time object that contains the product of the original Time and the number.
#Then use mul_time to write a function that takes a Time object that represents the finishing time
#in a race, and a number that represents the distance, and returns a Time object that represents the
#average pace (time per mile).


'''class Time(object):
    """ represents the time of day.
    attributes: hour, minute, second"""

time = Time()
time.hour = 3
time.minute = 0
time.second = 0


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    new_time = Time()
    minutes, new_time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def mul_time(time, multicand):
    time_int = time_to_int(time) * multicand
    new_time = int_to_time(time_int)
    if new_time.hour > 12:
        new_time.hour = new_time.hour % 12
#    print ("New time is: %.2d:%.2d:%.2d"
#    % (new_time.hour, new_time.minute, new_time.second))
    return new_time

# mul_time(time, 2)


def race_stats(time, distance):
    print ("The finish time was %.2d:%.2d:%.2d"
          % (time.hour, time.minute, time.second))
    print ("The distance was %d miles" % (distance))

    average = mul_time(time, (1.0 / distance))

    print ("The average is: %.2d:%.2d:%.2d per mile"
          % (average.hour, average.minute, average.second))

race_stats(time, 3)'''



#Exercise 16.7. The datetime module provides date and time objects that are similar to the Date
#and Time objects in this chapter, but they provide a rich set of methods and operators. Read the
#documentation at http: // docs. python. org/ 2/ library/ datetime. html .



'''import copy

# month:days in month
rules = {1: 31,
         2: 28,
         3: 31,
         4: 30,
         5: 31,
         6: 30,
         7: 31,
         8: 31,
         9: 30,
         10: 31,
         11: 30,
         12: 31}

names = {1: "January",
         2: "Feburary",
         3: "March",
         4: "April",
         5: "May",
         6: "June",
         7: "July",
         8: "August",
         9: "September",
         10: "October",
         11: "November",
         12: "December"}


class Date(object):
    """Representation of a date
    attributes: month, day, year"""

date = Date()
date.month = 10
date.day = 30
date.year = 2012


def increment_date(date, inc):
    date_ = copy.deepcopy(date)

    # adjust ui for leap year
#    if (date_.year % 4 == 0):
#        print "Starting: %s %s, %s (Leap year!)" \
#        % (names[date.month], date.day, date.year)
#    else:
#        print "Starting: %s %s, %s" % (names[date.month], date.day, date.year)
#    print "Moving forward %s days" %  inc
    while True:

        # adjust feb for leap year
        rules[2] = 28
        if (date_.year % 4 == 0):
            rules[2] = 29
        elif date_.month != 2:
            pass

        days_left = rules[date_.month] - date_.day

        # set date_.day based on value of days_left and inc
        if inc <= days_left:
            date_.day += inc
            break
        elif inc == 0:
            date_.day = rules[date_.month]
            break
        elif inc < 0:
            date_.day = rules[date_.month] + inc
            break
        else:
            inc -= rules[date_.month]
            date_.month += 1

        # increment year if month counter pushes past 12
        if date_.month > 12:
            date_.year += 1
            date_.month = 1

    # final adjustment of date if previous year was a leap year
    if ((date_.year - 1) % 4 == 0) and date_.month != 2:
        date_.day -= 1

    #final ui element
#    print "Ending: %s %s, %s" % (names[date_.month], date_.day, date_.year)
    return date_

newDate = increment_date(date, 365)

print (date, "%s %s, %s" % (names[date.month], date.day, date.year))
print (newDate, "%s %s, %s" % (names[newDate.month], newDate.day, newDate.year))
'''