#Exercise 13.1

'''from string import punctuation, whitespace

book = 'origin.txt'

with open(book, 'r') as fd:
    words = fd.read().split()


# remove punctuation, whitespace, uppercase
def clean(word):
    cleansed = ''
    for char in word:
        if ((char in punctuation) or (char in whitespace)):
            pass
        else:
            cleansed += char.lower()
    return cleansed


print "{} has {} 'words'".format(book, len([clean(word) for word in words]))'''


#Exercise 13.2

'''from string import punctuation, whitespace

origin = 'origin.txt'
huck = 'huck.txt'
frank = 'frank.txt'
great = 'great.txt'
meta = 'meta.txt'
sherlock = 'sherlock.txt'
tale = 'tale.txt'


def words(book):
    list_ = []
    flag = False
    signal = "*** START OF"
    for line in book:
        if flag == True:
            for word in line.split():
                list_.append(word)
        elif (signal in line) and (flag == False):
            flag = True
        else:
            pass
    return list_


def clean(word):
    result = ''
    for letter in word:
        if (letter in whitespace) or (letter in punctuation):
            pass
        else:
            result += letter.lower()
    return result


def histogram(data):
    hist = {}
    for word in data:
        hist[word] = hist.get(word, 0) + 1
    return hist


books = [origin, huck, frank, great, meta, sherlock, tale]


def stats():
    for book in books:
        book = open(book, 'r')
        print "Stats for %s:" % book.name
        data = [clean(word) for word in words(book)]
        book.close()
        print "  Total: %s" % len(data)
        print "  Unique: %s" % len(histogram(data))


stats()'''

#Exercise 13.3

'''from string import punctuation, whitespace

origin = 'origin.txt'
huck = 'huck.txt'
frank = 'frank.txt'
great = 'great.txt'
meta = 'meta.txt'
sherlock = 'sherlock.txt'
tale = 'tale.txt'

books = [origin, huck, frank, great, meta, sherlock, tale]


def words(book):
    list_ = []
    flag = False
    signal = "*** START OF"
    op = open(book, 'r')
    for line in op:
        if flag == True:
            for word in line.split():
                list_.append(word)
        elif (signal in line) and (flag == False):
            flag = True
        else:
            pass
    op.close()
    return list_


def clean(word):
    result = ''
    for char in word:
        if (char in whitespace) or (char in punctuation):
            pass
        else:
            result += char.lower()
    return result


def histogram(data):
    hist = {}
    for word in data:
        if word == '':
            pass
        else:
            hist[word] = hist.get(word, 0) + 1
    return hist


def main():
    for book in books:
        data = [clean(word) for word in words(book)]
        print "Stats for %s:" % book
        hist = histogram(data)
        top20 = []
        for key in hist:
            top20.append([hist[key], key])
        top20.sort(reverse=True)
        for i in range(0, 20):
            print "  %s) %s %s" % (i + 1, top20[i][1], top20[i][0])

        print "\n"


main()'''

#Exercise 13.4

'''from string import punctuation, whitespace

origin = 'origin.txt'  # Origin of Species, 1859
huck = 'huck.txt'  # Huck Finn, 1884
don = 'don.txt'  # Don Quixote, 1605
great = 'great.txt'  # Expectations, 1860
meta = 'meta.txt'  # morphisis, 1915
sherlock = 'sherlock.txt'  # 1887
divine = 'divine.txt'  # Comedy, 1308
journey = 'journey.txt'  # to the center of the earth, 1864

word_file = 'words.txt'
books = [origin, huck, don, great, meta, sherlock, divine, journey]


def words(book):
    list_ = []
    flag = False
    signal = "*** START OF"
    for line in book:
        if flag == True:
            for word in line.split():
                list_.append(word)
        elif (signal in line) and (flag == False):
            flag = True
        else:
            pass
    return list_


def clean(word):
    result = ''
    for char in word:
        if (char in whitespace) or (char in punctuation):
            pass
        elif not char.isalpha():
            pass
        else:
            result += char.lower()
    return result


def stats():
    for book in books:
        book_words = set([clean(word) for word in words(open(book, 'r'))])
        words_ = set([word for word in open(word_file, 'r')])
        print "Stats for %s" % open(book, 'r').name
        print "  There are %s non-listed words." % len(book_words - words_)


stats()

print "\n\nThe words not in the word list for origin.txt:"
print set([clean(word) for word in words(open(origin, 'r'))]) - \
      set([word for word in open(word_file, 'r')])'''



#Exercise 13.5

'''import random

t = ['a', 'a', 'b']


def hist(x):
    hist = {}
    for item in x:
        hist[item] = hist.get(item, 0) + 1
    return hist


hist = hist(t)


def choose_from_hist(hist):
    list_ = []
    for key in hist:
        for i in range(0, hist[key]):
            list_.append(key)
    return random.choice(list_)


def stats():
    a = 0
    b = 0
    for i in range(0, 10000):
        if choose_from_hist(hist) == 'a':
            a += 1
        else:
            b += 1
    print "a: %.5f" % (a / 10000.0), "b: %.5f" % (b / 10000.0)


stats()'''


#Exercise 13.8

'''from __future__ import print_function, division

import sys
import string
import random

# global variables
suffix_map = {}        # map from prefixes to a list of suffixes
prefix = ()            # current tuple of words


def process_file(filename, order=2):
    """Reads a file and performs Markov analysis.
    filename: string
    order: integer number of words in the prefix
    returns: map from prefix to list of possible suffixes.
    """
    fp = open(filename)
    skip_gutenberg_header(fp)

    for line in fp:
        if line.startswith('*** END OF THIS'):
            break

        for word in line.rstrip().split():
            process_word(word, order)


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS'):
            break


def process_word(word, order=2):
    """Processes each word.
    word: string
    order: integer
    During the first few iterations, all we do is store up the words;
    after that we start adding entries to the dictionary.
    """
    global prefix
    if len(prefix) < order:
        prefix += (word,)
        return

    try:
        suffix_map[prefix].append(word)
    except KeyError:
        # if there is no entry for this prefix, make one
        suffix_map[prefix] = [word]

    prefix = shift(prefix, word)


def random_text(n=100):
    """Generates random wordsfrom the analyzed text.
    Starts with a random prefix from the dictionary.
    n: number of words to generate
    """
    # choose a random prefix (not weighted by frequency)
    start = random.choice(list(suffix_map.keys()))

    for i in range(n):
        suffixes = suffix_map.get(start, None)
        if suffixes == None:
            # if the start isn't in map, we got to the end of the
            # original text, so we have to start again.
            random_text( n -i)
            return

        # choose a random suffix
        word = random.choice(suffixes)
        print(word, end=' ')
        start = shift(start, word)


def shift(t, word):
    """Forms a new tuple by removing the head and adding word to the tail.
    t: tuple of strings
    word: string
    Returns: tuple of strings
    """
    return t[1:] + (word,)


def main(script, filename='158-0.txt', n=100, order=2):
    try:
        n = int(n)
        order = int(order)
    except ValueError:
        print('Usage: %d filename [# of words] [prefix length]' % script)
    else:
        process_file(filename, order)
        random_text(n)
        print()


if __name__ == '__main__':
    main(*sys.argv)'''






#Exercise 13.9

'''from __future__ import print_function, division

import sys

import matplotlib.pyplot as plt

from analyze_book1 import process_file


def rank_freq(hist):
    """Returns a list of (rank, freq) tuples.
    hist: map from word to frequency
    returns: list of (rank, freq) tuples
    """
    # sort the list of frequencies in decreasing order
    freqs = list(hist.values())
    freqs.sort(reverse=True)

    # enumerate the ranks and frequencies
    rf = [(r+1, f) for r, f in enumerate(freqs)]
    return rf


def print_ranks(hist):
    """Prints the rank vs. frequency data.
    hist: map from word to frequency
    """
    for r, f in rank_freq(hist):
        print(r, f)


def plot_ranks(hist, scale='log'):
    """Plots frequency vs. rank.
    hist: map from word to frequency
    scale: string 'linear' or 'log'
    """
    t = rank_freq(hist)
    rs, fs = zip(*t)

    plt.clf()
    plt.xscale(scale)
    plt.yscale(scale)
    plt.title('Zipf plot')
    plt.xlabel('rank')
    plt.ylabel('frequency')
    plt.plot(rs, fs, 'r-', linewidth=3)
    plt.show()


def main(script, filename='emma.txt', flag='plot'):
    hist = process_file(filename, skip_header=True)

    # either print the results or plot them
    if flag == 'print':
        print_ranks(hist)
    elif flag == 'plot':
        plot_ranks(hist)
    else:
        print('Usage: zipf.py filename [print|plot]')


if __name__ == '__main__':
    main(*sys.argv)'''


