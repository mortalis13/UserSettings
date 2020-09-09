
# Creates folders from list

import sublime, sublime_plugin
import os, re

class CreateFoldersCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    folder = 'c:/in'
    
    names = [
      'a','b','c'
    ]
    
    for name in names:
      full_path = folder + name
      os.mkdir(full_path)
