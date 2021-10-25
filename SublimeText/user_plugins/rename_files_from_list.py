
# Renames all files in a folder using names from a text file
  
import sublime, sublime_plugin
import os, re, codecs

from user_modules.file_system_functions import *
from user_modules.general_functions import *


class RenameFilesFromListCommand(sublime_plugin.WindowCommand):
  def run(self):
    source_list = "path\\to\\file"
    dir_dest = "path\\to\\folder"
    
    filenames_src = []
    
    file = codecs.open(source_list, encoding='utf-8', mode='r')
    
    for line in file:
      line = line.rstrip('\r\n')
      line = normalize_filename(line)
      filenames_src.append(line)
    
    filenames_dest = get_filenames(dir_dest)
    
    i = 0
    
    for dest_file in filenames_dest:
      source_file = filenames_src[i]
      
      source_name, source_ext = os.path.splitext(source_file)
      dest_name, dest_ext = os.path.splitext(dest_file)
      
      from_name = dir_dest + "\\" + dest_file
      to_name = dir_dest + "\\" + source_name + dest_ext
      
      os.rename(from_name, to_name)
        
      i += 1
      
    print('finish')
    