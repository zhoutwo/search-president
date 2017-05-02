#!/usr/bin/env python
import math
import sys

from convert import *

k = 1.2
b = 0.75

def skip_bigram_helper(x):
  # Add stuff here if we want to handle sentence of length one.

  bigrams = [b for b in zip(x.split(" ")[:-1], x.split(" ")[1:])]
  skipgrams = [b for b in zip(x.split(" ")[:-2], x.split(" ")[2:])]
  skipbigrams = bigrams + skipgrams
  return skipbigrams
  
def IDF(N, nqi):
  return math.log10((N - nqi + 0.5) / (nqi + 0.5))
 
def cmpT(a, b):
	return sorted(a) == sorted(b)

def start():
  x = raw_input ("Enter the query you want to search. Enter q to quit.\n")
      
  skipbigrams = skip_bigram_helper(x)
  print(skipbigrams)

  # reading file 
  documentDict = convertAll('Presidents')
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
    for filename in documents:
      if skipbigram in documents[filename]:
        n[skipbigram] += 1
          
  score = dict()
  for filename in documentDict:
    score[filename] = 0
    for skipbigram in skipbigrams:
      D[skipbigram] = 0
      for documentBigram in documents[filename]:
        if documentBigram == skipbigram:
          D[skipbigram] += 1
    for skipbigram in skipbigrams:
      score[filename] += IDF(N, n[skipbigram]) * D[skipbigram] * (k + 1) / (D[skipbigram] + k * (1 - b + b * Davs[filename]))

  print score

		
	
	
if __name__ == '__main__':
  start()
