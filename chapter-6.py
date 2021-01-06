#Exercise 6.4. Draw a stack diagram for the following program. What does the program print?

'''def b(z):
        prod = a(z, z)
        print(z, prod)
        return prod

def a(x, y):
        x = x + 1
        return x * y

def c(x, y, z):
        total = x + y + z
        square = b(total)**2
        return square

x = 1
y = x + 1

print(c(x, y+3, x+y))'''




#Exercise 6.5. The Ackermann function, A(m, n), is defined:
#A(m, n) =
#n + 1 if m = 0
#A(m − 1, 1) if m > 0 and n = 0
#A(m − 1, A(m, n − 1)) if m > 0 and n > 0.
#See http: // en. wikipedia. org/ wiki/ Ackermann_ function . Write a function named ack
#that evaluates Ackermann’s function. Use your function to evaluate ack(3, 4), which should be
#125. What happens for larger values of m and n?



'''a = 3
b = 4

def ackermann(a, b):
    if a == 0:
        return b + 1
    elif b == 0:
        return ackermann(a - 1, 1)
    else:
        print('hello')
        return ackermann(a - 1, ackermann(a, b - 1))
ackermann(8, 5)'''



'''ex:6.6:  A palindrome is a word that is spelled the same backward and forward, like “noon”
and “redivider”. Recursively, a word is a palindrome if the first and last letters are the same and the
middle is a palindrome.'''



'''def fir(word):
    return word[0]


def las(word):
    return word[-1]


def mid(word):
    return word[1:-1]


def palindrome(word):
    if len(word) <= 1:
        return True
    if fir(word) != las(word):
        return False
    return palindrome(mid(word))


print(palindrome('sister'))
print(palindrome('MOM'))
print(palindrome('Brother'))
print(palindrome('python'))'''

'''ex:6.7:   A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a
function called is_power that takes parameters a and b and returns True if a is a power of b. Note:
you will have to think about the base case.'''


'''def power(a, b):
    while a % b == 0:
        if a == b:
            return True
        a /= b
    return False


print(power(10, 5))
print(power(2, 2))'''

'''ex:6.8:  The greatest common divisor (GCD) of a and b is the largest number that divides
both of them with no remainder.
One way to find the GCD of two numbers is based on the observation that if r is the remainder when
a is divided by b, then gcd(a, b) = gcd(b,r). As a base case, we can use gcd(a, 0) = a.'''


'''def gcd(a, b):
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)


print(gcd(22, 36))'''
