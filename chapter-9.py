#Exercise 9.7.

'''def searched_word(word):
    count = 0
    index = 0
    while index < len(word) - 1:
        if word[index] == word[index + 1]:
            count += 1
            if count == 3:
                return True
            index += 2
        else:
            count = 0
            index += 1


fin = open('words.txt')
count = 0

for line in fin:
    word = line.strip()
    if searched_word(word) == True:
        print(word)
        count += 1
print(count)'''



#Exercise 9.8.

'''def is_palindrome(word):
    return word == word[::-1]


def searched_number(number):
    if is_palindrome(str(number)[2:]):
        number += 1
        if is_palindrome(str(number)[1:]):
            number += 1
            if is_palindrome(str(number)[1:5]):
                number += 1
                if is_palindrome(str(number)):
                    return True
    return False


for num in range(100000, 1000000):
    if searched_number(num):
        print(num)'''



#Exercise 9.9.

#from __future__ import print_function, division


def str_fill(i, n):

    return str(i).zfill(n)


def are_reversed(i, j):

    return str_fill(i, 2) == str_fill(j, 2)[::-1]


def num_instances(diff, flag=False):

    daughter = 0
    count = 0
    while True:
        mother = daughter + diff


        if are_reversed(daughter, mother) or are_reversed(daughter, mother + 1):
            count = count + 1
            if flag:
                print(daughter, mother)
        if mother > 120:
            break
        daughter = daughter + 1
    return count


def check_diffs():

    diff = 10
    while diff < 70:
        n = num_instances(diff)
        if n > 0:
            print(diff, n)
        diff = diff + 1


print('diff  #instances')
check_diffs()

print()
print('daughter  mother')
num_instances(18, True)