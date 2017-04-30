#!/usr/bin/env python
from lib import html2text

def convertAll(folder):
  """ Converts all files in the folder to text """
  result = dict()
  for filename in os.listdir(folder):
    result[filename] = convert(os.path.join(folder, filename))
  return result

def convert(file):
  """ Converts a single file to text using html2text """
  h = html2text.HTML2Text()
  h.ignore_links = True
  h.ignore_images = True
  with open(file, "r") as currentFile:
    data = currentFile.readlines()
    currentFile.close()
    data = "".join(data).decode("utf-8")
    return h.handle(data)
