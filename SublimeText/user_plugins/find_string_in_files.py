
# Finds a RegExp string in all files from a specified directory
# Writes result to a text file

import sublime, sublime_plugin
import os, re, codecs

from user_modules.file_system_functions import *

class FindStringInFilesCommand(sublime_plugin.WindowCommand):
  def run(self):
    src_dir = "c:/dir"
    out_file_path = "c:/res_list.txt"
    pattern = 'text(\d\d)_\d{4}.pdf'
    
    group = 1
    
    ftlist = get_filenames_in_tree(src_dir)
    out_file = codecs.open(out_file_path, encoding='utf-8', mode='w')
    
    for item in ftlist:
      text = find_in_file(item, pattern, group)
      out_file.write(text + '\n')
      
    out_file.close()
    
    print('\nfinish')


def find_in_file(file_path, pattern, group=False):
  file = codecs.open(file_path, encoding='utf-8', mode='r')
  doc = file.read()
  text = ''
  
  match = re.search(pattern, doc)
  if match:
    text = match.group(group)
    
  file.close()
  
  return text
  