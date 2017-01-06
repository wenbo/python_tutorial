# -*- coding:utf-8 -*-
# Filename: sinica_treebank.py
# Author：hankcs
# Date: 2014-04-08 上午11:44
from __future__ import print_function
import nltk
import sqlite3
from nltk.corpus import sinica_treebank
 
sinica_text = nltk.Text(sinica_treebank.words())
print(sinica_text)
for (key, var) in sinica_treebank.tagged_words()[:8]:
    print('%s/%s' % (key, var))

print(sinica_text.concordance('我'))
print(sinica_text.concordance(u'\u5609\u73cd'))
print("************* sinica_fd=nltk.FreqDist(sinica_treebank.words()) NLTK计算中文高频词 **********")
sinica_fd=nltk.FreqDist(sinica_treebank.words())
top100=sinica_fd.items()[0:100]
for (x,y) in top100:
    print(x,y)
