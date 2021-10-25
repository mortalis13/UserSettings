
# Renames file from a list of lines according to a pattern applied to each line

import sublime, sublime_plugin
import os, re, codecs

from user_modules.file_system_functions import *
from user_modules.general_functions import *


class RenameFilesFromMapCommand(sublime_plugin.WindowCommand):
    
  def run(self):
    view = self.window.show_input_panel('Folder Path: ', '', self.on_done, None, None)
    
    
  def on_done(self, folder):
    print('\nRenaming files ...')
    map_file_path = "c:/map.txt"
    
    map_file = codecs.open(map_file_path, encoding='utf-8', mode='r')
    map_lines = map_file.readlines()
    map_file.close()
    
    res_map = {}
    
    for map_line in map_lines:
      map_line = map_line.strip()
      key, val = map_line.split(' >> ')
      
      val = normalize_filename(val)
      res_map[key] = val
    
    
    ftlist = get_filenames_in_tree(folder)
    
    for from_file_path in ftlist:
      path = os.path.dirname(from_file_path)
      file_name = os.path.basename(from_file_path)
      
      from_name, from_ext = os.path.splitext(file_name)
      if not from_name in res_map:
        continue
        
      to_file_path = path + '/' + res_map[from_name] + from_ext
      to_file_path = os.path.normpath(to_file_path)
      
      # print(from_file_path, to_file_path)
      os.rename(from_file_path, to_file_path)
      
      
    print('\nfinish')
