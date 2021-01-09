#Exercise 11.1

'''import uuid

with open('words.txt') as fd:
    words = fd.read().splitlines()

result = dict()


def dictionary():
    for line in words:
        result[line] = uuid.uuid4()
    return result

print (dictionary())'''



#Exercise 11.2

'''def histogram(word):
    dictionary = dict()
    for character in word:
        dictionary[character] = 1 + dictionary.get(character, 0)
    return dictionary

print histogram('antidisestablishmentarianism')'''

#Exercise 11.3

'''def histogram(word):
    dictionary = dict()
    for letter in word:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary


def print_hist(histogram):
    histoList = histogram.keys()
    histoList.sort()
    for letter in histoList:
        print letter, histogram[letter]

h = histogram('parrot')
print_hist(h)'''

#Exercise 11.4

'''def reverse_lookup(dictionary, value):
    results = []
    for key in dictionary:
        if dictionary[key] == value:
            results.append(key)
    return results


def histogram(word):
    dictionary = dict()
    for letter in word:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary

h = histogram('parrot')
k = reverse_lookup(h, 2)
print (k)'''


#Exercise 11.5

'''def histogram(word):
    dictionary = dict()
    for letter in word:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary


def invert_dict(d):
    inv = dict()
    for key in d:
        val = d[key]
        inv.setdefault(val, [])
        inv[val].append(key)
    return inv

hist = histogram('parrot')
# print hist
inv = invert_dict(hist)
print (inv)'''

#Exercise 11.6

'''known = {0: 0, 1: 1}


def fibonacci(n):
    if n in known:
        return known[n]
    else:
        res = fibonacci(n - 1) + fibonacci(n - 2)
    known[n] = res
    return res

#def fibonacci(n):
#    if n == 0:
#        return 0
#    elif n == 1:
#        return 1
#    else:
#        return fibonacci(n - 1) + fibonacci(n - 2)

print fibonacci(40)'''


#Exercise 11.8

'''listOne = [1, 2, 3, 4, 5, 5]


def has_dups(myList):
    dictionary = {}
    for item in myList:
        dictionary[item] = 1 + dictionary.get(item, 0)
        if dictionary[item] > 1:
            return True
    return False

print (has_dups(listOne))'''



'''Exercise 11.9. If you did Exercise 10.8, you already have a function named has_duplicates that
takes a list as a parameter and returns True if there is any object that appears more than once in the
list.
Use a dictionary to write a faster, simpler version of has_duplicates'''


'''list = [1, 2, 3, 4, 5, 5]


def has_duplicates(myList):
    dicti = {}
    for item in myList:
        dicti[item] = 1 + dicti.get(item, 0)
        if dicti[item] > 1:
            return True
    return False

print (has_duplicates(list))'''

'''Exercise 11.10. Two words are “rotate pairs” if you can rotate one of them and get the other (see
rotate_word in Exercise 8.12).
Write a program that reads a wordlist and finds all the rotate pairs.'''


'''def make_dict(file_input):
    diction = dict()
    word_list = []

    fin = open(file_input)
    for line in fin:
        word = line.strip()
        word_list.append(word)

    index = 0
    for word in word_list:
        diction[word] = index
        index += 1
    return diction


def rotate_word(word, shift):
    rotate = ''
    for let in word:
        rotate += chr(ord(let) + shift)
    return rotate


def rotate_pairs(word_dict):
    pairs = {}
    for let in range(1, 27):
        for word in word_dict:
            if rotate_word(word, let) in word_dict:
                if word in pairs:
                    pairs[word].append((rotate_word(word, let), let))
                else:
                    pairs[word] = [(rotate_word(word, let), let)]
    return pairs


diction = make_dict("words.txt")
print(rotate_pairs(diction))'''




#Exercise 11.11.

'''from __future__ import print_function, division

from pronounce import read_dictionary


def make_word_dict():
    """Read. the words in words.txt and return a dictionary
    that contains the words as keys."""
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = word

    return d


def homophones(a, b, phonetic):
    """Checks if words two can be pronounced the same way.
    If either word is not in the pronouncing dictionary, return False
    a, b: strings
    phonetic: map from words to pronunciation codes
    """
    if a not in phonetic or b not in phonetic:
        return False

    return phonetic[a] == phonetic[b]


def check_word(word, word_dict, phonetic):
    """Checks to see if the word has the following property:
    removing the first letter yields a word with the same
    pronunciation, and removing the second letter yields a word
    with the same pronunciation.
    word: string
    word_dict: dictionary with words as keys
    phonetic: map from words to pronunciation codes
    """
    word1 = word[1:] 
    if word1 not in word_dict:
        return False
    if not homophones(word, word1, phonetic):
        return False

    word2 = word[0] + word[2:]
    if word2 not in word_dict:
        return False
    if not homophones(word, word2, phonetic):
        return False

    return True


if __name__ == '__main__':
    phonetic = read_dictionary()
    word_dict = make_word_dict()

    for word in word_dict:
        if check_word(word, word_dict, phonetic):
            print(word, word[1:], word[0] + word[2:])'''