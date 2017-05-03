#!/usr/bin/env python
from externalLib import html2text
from htmlreader import *
import os

def convertAll(folder):
  """ Converts all files in the folder to text """
  result = dict()
  reader = HtmlPageReader()
  for filename in os.listdir(folder):
    path = os.path.join(folder, filename)
    content = convert(path).encode("UTF-8")
    reader.setPath(path)
    name = reader.getTitle().decode("UTF-8")
    name = name[0:len(name) - 12]
    result[name] = content
  return result

def convert(file):
  """ Converts a single file to text using html2text """
  h = html2text.HTML2Text()
  h.ignore_links = True
  h.ignore_images = True
  with open(file, "r") as currentFile:
    data = currentFile.readlines()
    currentFile.close()
    data = "".join(data).decode("UTF-8")
    return h.handle(data)
