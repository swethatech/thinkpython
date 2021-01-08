#Exercise 7.1.

'''import math

def mysqrt(a):

    x = a / 2
    while True:
        estimated_root = (x + a / x) / 2
        if estimated_root == x:
            return estimated_root
            break
        x = estimated_root


def test_square_root(list_of_a):

    line1a = "a"
    line1b = "mysqrt(a)"
    line1c = "math.sqrt(a)"
    line1d = "diff"

    line2a = "-"
    line2b = "---------"
    line2c = "------------"
    line2d = "----"

    spacing1 = " "
    spacing2 = " " * 3
    spacing3 = ""

    print(line1a, spacing1, line1b, spacing2, line1c, spacing3, line1d)
    print(line2a, spacing1, line2b, spacing2, line2c, spacing3, line2d)

    for a in list_of_a:
        col1 = float(a)
        col2 = mysqrt(a)
        col3 = math.sqrt(a)
        col4 = abs(mysqrt(a) - math.sqrt(a))

        print(col1, "{:<13f}".format(col2), "{:<13f}".format(col3), col4)


test_square_root(range(1, 10))'''




#Exercise 7.2.


'''def eval_loop():
    
    while True:
        user_input = input(">>> ")

        if eval(user_input) == 'done':
            break
        print(eval(user_input))

    return eval(user_input)


eval_loop()'''


#>>> eval('1 + 2 * 3')
#7
#>>> import math
#>>> eval('math.sqrt(5)')
#2.2360679774997898
#>>> eval('type(math.pi)')
#<class 'float'>



#Exercise 7.3.


#from __future__ import print_function, division

'''import math


def factorial(n):
    """Computes factorial of n recursively."""
    if n == 0:
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        return result


def estimate_pi():
    """Computes an estimate of pi.
    Algorithm due to Srinivasa Ramanujan, from
    http://en.wikipedia.org/wiki/Pi
    """
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = factorial(4 * k) * (1103 + 26390 * k)
        den = factorial(k) ** 4 * 396 ** (4 * k)
        term = factor * num / den
        total += term

        if abs(term) < 1e-15:
            break
        k += 1

    return 1 / total


print(estimate_pi())'''




