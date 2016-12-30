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
