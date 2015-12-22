# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 16:49:25 2015

@author: hovin
"""
with open('C:\\cygwin\\srilm\\b1-c01e.txt') as f:
    corpus = f.read()
    corpus = corpus.split()
    vocal = []
    for word in corpus:
        if word not in vocal:
            vocal.append(word)
    vocal.sort() # sorts normally by alphabetical order
    vocal.sort(key=len, reverse=False) # sorts by descending length
with open('C:\\cygwin\\srilm\\corpus.txt', 'w') as f:
    for word in vocal:
        f.write(word + '\n')
