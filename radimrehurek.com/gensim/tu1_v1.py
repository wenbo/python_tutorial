# -*- coding:utf-8 -*-
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim import corpora, models, similarities


documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]


# documents = ["小明 2005 年  毕业  于  北京  清华大学",
#              "小王 2006 年  毕业  于  北京  清华大学"
#              ]

# remove common words and tokenize
stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in documents]

# remove words that appear only once
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1]
         for text in texts]

from pprint import pprint   # pretty-printer
pprint(texts)

dictionary = corpora.Dictionary(texts)
dictionary.save('/tmp/deerwester.dict') # store the dictionary, for future reference
print(dictionary)

print(dictionary.token2id)
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('/tmp/deerwester.mm', corpus) # store to disk, for later use
print(corpus)

#  new_doc = "Human computer interaction"
#  new_vec = dictionary.doc2bow(new_doc.lower().split())
#  print(new_vec) # the word "interaction" does not appear in the dictionary and is ignored

#  corpus = [dictionary.doc2bow(text) for text in texts]
#  corpora.MmCorpus.serialize('/tmp/deerwester.mm', corpus) # store to disk, for later use
#  print(corpus)

#  class MyCorpus(object):
#      def __iter__(self):
#          for line in open('mycorpus.txt'):
#              # assume there's one document per line, tokens separated by whitespace
#              yield dictionary.doc2bow(line.lower().split())

#  corpus_memory_friendly = MyCorpus() # doesn't load the corpus into memory!
#  print(corpus_memory_friendly)

#  for vector in corpus_memory_friendly: # load one vector into memory at a time
#      print(vector)

#  # collect statistics about all tokens
#  dictionary = corpora.Dictionary(line.lower().split() for line in open('mycorpus.txt'))
#  # remove stop words and words that appear only once
#  stop_ids = [dictionary.token2id[stopword] for stopword in stoplist
#              if stopword in dictionary.token2id]
#  once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
#  dictionary.filter_tokens(stop_ids + once_ids) # remove stop words and words that appear only once
#  dictionary.compactify() # remove gaps in id sequence after words that were removed
#  print(dictionary)

#  from gensim import corpora
#  # create a toy corpus of 2 documents, as a plain Python list
#  corpus = [[(1, 0.5)], []]  # make one document empty, for the heck of it

#  corpora.MmCorpus.serialize('/tmp/corpus.mm', corpus)

#  corpora.SvmLightCorpus.serialize('/tmp/corpus.svmlight', corpus)
#  corpora.BleiCorpus.serialize('/tmp/corpus.lda-c', corpus)
#  corpora.LowCorpus.serialize('/tmp/corpus.low', corpus)

#  corpus = corpora.MmCorpus('/tmp/corpus.mm')

#  print(corpus)
# orpus(2 documents, 2 features, 1 non-zero entries)

#  # one way of printing a corpus: load it entirely into memory
#  print(list(corpus)) # calling list() will convert any sequence to a plain Python list
# 1, 0.5)], []]

#  # another way of doing it: print one document at a time, making use of the streaming interface
#  for doc in corpus:
#      print(doc)
# , 0.5)]


#  corpora.BleiCorpus.serialize('/tmp/corpus.lda-c', corpus)

#  corpus = gensim.matutils.Dense2Corpus(numpy_matrix)
#  numpy_matrix = gensim.matutils.corpus2dense(corpus, num_terms=number_of_corpus_features)


#  corpus = gensim.matutils.Sparse2Corpus(scipy_sparse_matrix)
#  scipy_csc_matrix = gensim.matutils.corpus2csc(corpus)
