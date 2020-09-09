
# Writes all filenames to a text file

import sublime, sublime_plugin
import os, re, codecs

from .modules.file_system_functions import *


class ListAllFilesCommand(sublime_plugin.WindowCommand):
    
  def run(self):
    view = self.window.show_input_panel('Folder Path:', '', self.on_done, None, None)
    
  def on_done(self, folder):
    out_file = "c:/res_list_tree.txt"

    ftlist = get_filenames_in_tree(folder)
    res_file = codecs.open(out_file, encoding='utf-8', mode='w')
    
    for item in ftlist:
      item = item.replace('\\','/')
      line = item + '\n'
      res_file.write(line)
      
    res_file.close()
    
    print('\nfinish')
