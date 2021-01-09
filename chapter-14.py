'''Exercise 14.1. The os module provides a function called walk that is similar to this one but more
versatile. Read the documentation and use it to print the names of the files in a given directory and
its subdirectories.'''

'''import os
import time


def run():
    direct = raw_input('name of dir ')
    flist = []
    for x, y, z in os.walk(direct):
        if len(z) > 0:
            flist.extend(z)
    print (direct)
    for x in flist:
        print (x)
        time.sleep(1)'''


#Exercise 14.2

'''import os

cwd = os.getcwd()

for one, two, three in os.walk(cwd):
    print one, three'''



'''Exercise 14.3. If you download my solution to Exercise 12.4 from http: // thinkpython. com/
code/ anagram_ sets. py , you’ll see that it creates a dictionary that maps from a sorted string of
letters to the list of words that can be spelled with those letters. For example, 'opst' maps to the
list ['opts', 'post', 'pots', 'spot', 'stop', 'tops'].
Write a module that imports anagram_sets and provides two new functions: store_anagrams
should store the anagram dictionary in a “shelf;” read_anagrams should look up a word and return
a list of its anagrams.'''


'''import pickle

def anagrams_sets(wlist):
    d=dict()
    for word in wlist:
        a=list(word)
        a.sort()
        a=tuple(a)
        d[a]=d.get(a,[])+[word]
    return d

def stored_anagrams(d):
    a=raw_input('read or write ')    
    if a == 'write':
        f=open('yoga.db','w')
        f.write(pickle.dumps(d))
    elif a=='read':
        f=open('yoga.db')
        s=''.join(f.readlines())
        s=pickle.loads(s)
        for x in s:
            d[x]=s[x]
    f.close()'''









'''Exercise 14.4. In a large collection of MP3 files, there may be more than one copy of the same song,
stored in different directories or with different file names. The goal of this exercise is to search for
duplicates.'''


'''def files(dirf):
    import os 
    mlist=[]
    for x,y,z in os.walk(dirf):
        if len(z)>0:
            for i in z:
                if i[-1]=='3':
                    mlist.append(x+'/'+i)
    return mlist'''





'''Write a function called sed that takes as arguments a pattern string, a replacement
string, and two filenames; it should read the first file and write the contents into the second file
(creating it if necessary). If the pattern string appears anywhere in the file, it should be replaced
with the replacement string.
14.6. Databases 137
If an error occurs while opening, reading, writing or closing files, your program should catch the
exception, print an error message, and exit. '''


'''def sed_pattern(pat,rep,rfile,wfile):
    try:
        r=open(rfile)
        w=open(wfile,'w')
        a='a'
        text=''
        while a != '':
            a=r.readline()
            text+=a
        while pat in text:
            p=text.find(pattern)
            text=text[:p]+rep+text[p+len(pat):]
        w.write(text)
        r.close()
        w.close()
    except:
        return 'file not found'     '''








