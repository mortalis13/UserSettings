
# Creates folders in the file system
# First line is the destination folder
# all the next lines - folder names to create in the first one

import sublime, sublime_plugin
import os, re

class CreateFoldersFromSelectionCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    folder = '/'
    
    view = self.view
    r=sublime.Region(0, view.size())
    lines = view.lines(r)
    
    folders_count = 0
    first_line = True
    
    for line in lines:
      if first_line:
        folder = view.substr(line).strip()
        first_line = False
      else:
        name = view.substr(line).strip()
        
        if not len(name) == 0:
          full_path = folder + '/' + name
          if not os.path.exists(full_path):
            os.mkdir(full_path)
            folders_count += 1
      
    print('Folders created:', folders_count)
    