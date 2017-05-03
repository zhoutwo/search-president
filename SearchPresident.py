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
  for name in documentDict:
    lengths[name] = len(documentDict[name])     
    total_length += lengths[name]
    
  avg_length = total_length / N
    
  Davs = dict()
  for name in documentDict:
    Davs[name] = 1.0 * lengths[name] / avg_length

  # n counts for the number of documents that this word appears in.
  n = 0
  for name in documentDict:
    a = 0
    document = documentDict[name].lower().split(" ")
    for word in document:
      if word == x:
        a += 1
    if a > 5:
      n += 1
   
  # D = number of time this bigram appears in a file      
  score = dict()
  for name in documentDict:
    D = 0
    document = documentDict[name].lower().split(" ")
    for word in document:
      if word == x:
        D += 1
    score[name] = abs(IDF(N, n)) * D * (k + 1) / (D + k * (1 - b + b * Davs[name]))

  return score

def printScores(scoreTuples):
  print "Results:"
  for t in scoreTuples:
    if str(t[0]) != "0.0":
      print t[1], t[0]
  print "(End of result)"
  print ""

def start():
  # Reading file 
  print "Reading files"
  documentDict = convertAll('Presidents')
  while (True):
    x = raw_input ("Enter the query you want to search. Enter q to quit.\n")
    if x == "q":
      exit()
    y = x.split(" ")
    if len(y) == 0:
      print "Input invalid"
      exit()
    elif len(y) == 1:
      score = BM25Scoring(x, documentDict)
      scoreTuples = []
      for name in score:
        scoreTuples.append((score[name], name))
      scoreTuples.sort(reverse=True)
      printScores(scoreTuples)
    else:
      skipbigrams = skip_bigram_helper(x)
  
      documents = dict()
      for name in documentDict:
        documents[name] = skip_bigram_helper(documentDict[name])
        
      # N = number of documents
      N = len(documents)
      # count = number of words occuring in each documents
      # D(name, bigram) = number of time this bigram appears in name
      Davs = dict()
      D = dict()
      total_length = 0
      lengths = dict()
  
      for name in documentDict:
        lengths[name] = len(documentDict[name])     
        total_length += lengths[name]
        
      avg_length = total_length / N
        
      for name in documents:
        Davs[name] = 1.0 * lengths[name] / avg_length
        
      n = dict()
      a = dict()
        
      for skipbigram in skipbigrams:
        n[skipbigram] = 0
        for name in documentDict:
          a[name] = 0
          document = documents[name]
          for bigram in document:
            if bigram == skipbigram:
              a[name] += 1
          if a[name] > 0:
            n[skipbigram] += 1
        i = 0
        while n[skipbigram] >= N / 2:
          i += 1
          n[skipbigram] = 0
          for name in documentDict:
            if a[name] > i:
              n[skipbigram] += 1
              
      score = dict()
      for name in documentDict:
        score[name] = 0
        for skipbigram in skipbigrams:
          D[skipbigram] = 0
          for documentBigram in documents[name]:
            if documentBigram == skipbigram:
              D[skipbigram] += 1
        for skipbigram in skipbigrams:
          score[name] += len(skipbigram) * len(skipbigram) * IDF(N, n[skipbigram]) * D[skipbigram] * (k + 1) / (D[skipbigram] + k * (1 - b + b * Davs[name]))

      scoreTuples = []
      for name in score:
        scoreTuples.append((score[name], name))
      scoreTuples.sort(reverse=True)
      printScores(scoreTuples)
	
if __name__ == '__main__':
  start()
