#!/usr/bin/env python
import math
import sys

from convert import *

k = 1.2
b = 0.75

def skip_bigram_helper(x):
  # Add stuff here if we want to handle sentence of length one.

  x = x.replace(",", "").replace(".", "").lower()
  bigrams = [b for b in zip(x.split(" ")[:-1], x.split(" ")[1:])]
  skipgrams = [b for b in zip(x.split(" ")[:-2], x.split(" ")[2:])]
  skipbigrams = bigrams + skipgrams + [(ele,) for ele in x.split(" ")]
  return skipbigrams
  
def IDF(N, nqi):
  return math.log10((N - nqi + 0.5) / (nqi + 0.5))
 
def cmpT(a, b):
	return sorted(a) == sorted(b)

def BM25Scoring(x, documentDict):
  x = x.lower()
    
  # N = number of documents
  N = len(documentDict)
  
  total_length = 0
  lengths = dict()
  for filename in documentDict:
    lengths[filename] = len(documentDict[filename])     
    total_length += lengths[filename]
    
  avg_length = total_length / N
    
  Davs = dict()
  for filename in documentDict:
    Davs[filename] = 1.0 * lengths[filename] / avg_length

  # n counts for the number of documents that this word appears in.
  n = 0
  for filename in documentDict:
    a = 0
    document = documentDict[filename].lower().split(" ")
    for word in document:
      if word == x:
        a += 1
    if a > 5:
      n += 1
   
  # D = number of time this bigram appears in a file      
  score = dict()
  for filename in documentDict:
    D = 0
    document = documentDict[filename].lower().split(" ")
    for word in document:
      if word == x:
        D += 1
    print (N, D, n)
    score[filename] = abs(IDF(N, n)) * D * (k + 1) / (D + k * (1 - b + b * Davs[filename]))
  # print (N, D, n)

  return score


def start():
  # Reading file 
  print "Reading files"
  documentDict = convertAll('Presidents')
  while (True):
    x = raw_input ("Enter the query you want to search. Enter q to quit.\n")
    if x == "q":
      exit()
    y = x.split(" ")
    # print len(x)
    if len(y) == 0:
      print "Input invalid"
      exit()
    elif len(y) == 1:
      score = BM25Scoring(x, documentDict)
      scoreTuples = []
      for filename in score:
        scoreTuples.append((score[filename], filename))
      scoreTuples.sort(reverse=True)
      print scoreTuples
    else:
      skipbigrams = skip_bigram_helper(x)
      print(skipbigrams)
  
      documents = dict()
      for filename in documentDict:
        documents[filename] = skip_bigram_helper(documentDict[filename])
        
      # N = number of documents
      N = len(documents)
      # count = number of words occuring in each documents
      # D(filename, bigram) = number of time this bigram appears in filename
      Davs = dict()
      D = dict()
      total_length = 0
      lengths = dict()
  
      for filename in documentDict:
        lengths[filename] = len(documentDict[filename])     
        total_length += lengths[filename]
        
      avg_length = total_length / N
        
      for filename in documents:
        Davs[filename] = 1.0 * lengths[filename] / avg_length
        
      n = dict()
        
      for skipbigram in skipbigrams:
        n[skipbigram] = 0
        for filename in documentDict:
          a = 0
          document = documents[filename]
          for bigram in document:
            if bigram == skipbigram:
              a += 1
          if a > 5:
            n[skipbigram] += 1
              
      score = dict()
      for filename in documentDict:
        score[filename] = 0
        for skipbigram in skipbigrams:
          D[skipbigram] = 0
          for documentBigram in documents[filename]:
            if documentBigram == skipbigram:
              D[skipbigram] += 1
        print N, D, n
        for skipbigram in skipbigrams:
          score[filename] += IDF(N, n[skipbigram]) * D[skipbigram] * (k + 1) / (D[skipbigram] + k * (1 - b + b * Davs[filename]))
  
#       for word in y:
#         score2 = BM25Scoring(x, documentDict)
#         for filename in documentDict:
#           score[filename] += score2[filename]
      scoreTuples = []
      for filename in score:
        scoreTuples.append((score[filename], filename))
      scoreTuples.sort(reverse=True)
      print scoreTuples
	
if __name__ == '__main__':
  start()
