import math
import sys


class SearchPresident:

	def __init__(self):
		pass

	def start():
		
		x = raw_input ("Enter the query you want to search. Enter q to quit.\n")
		

		# Add stuff here if we want to handle sentence of length one.

		bigrams = [b for b in zip(x.split(" ")[:-1], x.split(" ")[1:])]
		skipgrams = [b for b in zip(x.split(" ")[:-2], x.split(" ")[2:])]
		skipbigrams = bigrams + skipgrams
		
		print(skipbigrams)







	if __name__ == '__main__':
  		start()