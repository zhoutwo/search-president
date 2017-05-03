#!/usr/bin/env python
from selenium import webdriver
import os

class HtmlPageReader(object):
  
  def __init__(self):
    self.driver = webdriver.PhantomJS(executable_path="./externalLib/phantomjs.exe")
    
  def setPath(self, path):
    path = ("file:///" + os.path.abspath(path)).replace("\\", "/")
    self.driver.get(path)
    
  def getTitle(self):
    return self.driver.title
