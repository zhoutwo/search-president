#!/usr/bin/env python
import math
import sys

def skip_bigram_helper(x):
	# Add stuff here if we want to handle sentence of length one.

	bigrams = [b for b in zip(x.split(" ")[:-1], x.split(" ")[1:])]
	skipgrams = [b for b in zip(x.split(" ")[:-2], x.split(" ")[2:])]
	skipbigrams = bigrams + skipgrams
	return skipbigrams

def start():
	x = raw_input ("Enter the query you want to search. Enter q to quit.\n")
	
	skipbigrams = skip_bigram_helper(x)
	#print(skipbigrams)

	#reading file 




	bigrams
	
	# N = number of documents
	# NDocuments = number of words occuring in each documents
	# 
	for ()

if __name__ == '__main__':
	start()
