
# Renames files from the list in the current view

import sublime, sublime_plugin
import os, re, codecs

from user_modules.file_system_functions import *
from user_modules.general_functions import *

  
class RenameFilesFromSelectionCommand(sublime_plugin.WindowCommand):
  def run(self):
    view = self.window.show_input_panel('Folder Path:', '', self.on_done, None, None)
    
  def on_done(self, folder):
    print('\nTrying to rename files in folder: ' + folder)
    print('...')
    
    view = self.window.active_view()
    r=sublime.Region(0, view.size())
    lines = view.lines(r)
    
    filenames_src = []
    
    for line in lines:
      text = view.substr(line)
      text = normalize_filename(text)
      filenames_src.append(text)
    
    filenames_dest = get_filenames(folder)
    filenames_dest = sorted(filenames_dest, key=natural_key)
    
    i = 0
    
    for dest_file in filenames_dest:
      source_file = filenames_src[i]
      
      source_name, source_ext = os.path.splitext(source_file)
      dest_name, dest_ext = os.path.splitext(dest_file)
      
      from_name = folder + "\\" + dest_file
      to_name = folder + "\\" + source_name + dest_ext
      
      # print(from_name + '\n' + to_name + '\n')
      os.rename(from_name, to_name)
        
      i += 1
    
    print('\nfinish')


# See http://www.codinghorror.com/blog/archives/001018.html
def natural_key(string_):
  return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_)]
  
