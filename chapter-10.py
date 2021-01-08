#Exercise 10.6.

'''def is_sorted(li):
    return li == sorted(li)


print(is_sorted([1, 2, 2]))
print(is_sorted(['b', 'a']))
print(is_sorted(['a', 'a']))
print(is_sorted(['a', 'b']))
print(is_sorted([2, 1]))
print(is_sorted([1, 2, 3, 4, 3]))'''


#Exercise 10.7.

'''def is_anagram(text1, text2):
    return sorted(text1) == sorted(text2)

print(is_anagram('abba', 'baba'))
print(is_anagram('lol', 'kol'))
print(is_anagram('a', 'b'))
print(is_anagram('', 'a'))'''


#Exercise 10.8

'''def has_duplicates(li):
    if len(li) == 0:
        return "List is empty."
    elif len(li) == 1:
        return "List contains only one element."

    previous_elem = li[0]
    for elem in sorted(li):
        if previous_elem == elem:
            return True
        previous_elem = elem
    return False


t = [4, 7, 2, 7, 3, 8, 9]
print(has_duplicates(t))
print(has_duplicates(['b', 'd', 'a', 't']))
print(has_duplicates([]))
print(has_duplicates(['']))
print(has_duplicates([5, 7, 9, 2, 4, 1, 8, ]))'''

#Exercise 10.9

'''from random import randint


def date_generator(pupils):
    dates = []
    for student in range(pupils):
        dates.append(randint(1, 366))
    return dates


def has_matches(dates):
    dates.sort()
    for i in range(len(dates) - 1):
        if dates[i] == dates[i + 1]:
            return True
    return False


def chances(num_of_simulations, pupils):
    matches = 0

    for i in range(num_of_simulations):
        dates = date_generator(pupils)
        if has_matches(dates):
            matches += 1

    print("There are {} classes having students with the same birthday date".format(matches))
    print("in {} simulations.".format(num_of_simulations))


chances(1000, 23)
'''






#Exercise 10.10.

'''def version1(file):
    fin = open(file)
    li = []

    for line in fin:
        word = line.strip()
        li.append(word)

    return li


def version2(file):
    fin = open(file)
    t = []

    for line in fin:
        x = line.strip()
        t = t + [x]'''

#Exercise 10.11
#from __future__ import print_function, division

'''import bisect

def make_word_list():

    word_list = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


def in_bisect(word_list, word):

    if len(word_list) == 0:
        return False

    i = len(word_list) // 2
    if word_list[i] == word:
        return True

    if word_list[i] > word:
        # search the first half
        return in_bisect(word_list[:i], word)
    else:
        # search the second half
        return in_bisect(word_list[i + 1:], word)


def in_bisect_cheat(word_list, word):

    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False

    return word_list[i] == word


if __name__ == '__main__':
    word_list = make_word_list()

    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'in list', in_bisect(word_list, word))

    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'in list', in_bisect_cheat(word_list, word))'''






#Exercise 10.12.

'''import bisect

def word_list(file):
    fin = open(file)
    li = []

    for line in fin:
        word = line.strip()
        li.append(word)
    return li


def in_bisect_cheat(word_list, word):
    """Checks whether a word is in a list using bisection search.
    Precondition: the words in the list are sorted
    word_list: list of strings
    word: string
    """
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False

    return word_list[i] == word


def reverse_pair(li):
    list_of_pairs = []
    for word in li:
        if in_bisect_cheat(li, word[::-1]):
            pair = (word, word[::-1])
            list_of_pairs.append(pair)
    return list_of_pairs


li = word_list("words.txt")
print(reverse_pair(li))'''




#Exercise 10.13

'''from inlist import make_word_list, in_bisect


def interlock(word_list, word):
    """Checks whether a word contains two interleaved words.
    word_list: list of strings
    word: string
    """
    evens = word[::2]
    odds = word[1::2]
    return in_bisect(word_list, evens) and in_bisect(word_list, odds)


def interlock_general(word_list, word, n=3):
    """Checks whether a word contains n interleaved words.
    word_list: list of strings
    word: string
    n: number of interleaved words
    """
    for i in range(n):
        inter = word[i::n]
        if not in_bisect(word_list, inter):
            return False
    return True


if __name__ == '__main__':
    word_list = make_word_list()

    for word in word_list:
        if interlock(word_list, word):
            print(word, word[::2], word[1::2])

    for word in word_list:
        if interlock_general(word_list, word, 3):
            print(word, word[0::3], word[1::3], word[2::3])'''