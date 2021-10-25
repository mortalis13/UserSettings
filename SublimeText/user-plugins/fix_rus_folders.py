
# Fixes russian filenames/text from cp850 encoding
# (met this problem when unzipped archives downloaded from Google Drive)
# starts from the dir src_dir and recursively fixes all file/folder names in it
# names with latin characters remain the same

import sublime, sublime_plugin
import os

from user_modules.file_system_functions import *


class FixRusFoldersCommand(sublime_plugin.WindowCommand):
  def run(self, folder):
    self.show_input_panel('Folder Path:', folder)
    
    # folder = "path\\to\\folder"
  
  
  def on_done(self, folder):
    print('\nTrying to fix folder: ' + folder)
    
    src_dir = fix_name(folder)
    fix_names(src_dir)
    
    print('\nfinish')
    
  def show_input_panel(self, label, folder):
    view = self.window.show_input_panel(label, folder, self.on_done, None, None)


def fix_name(dir, item = ''):
  if item == '':
    item = os.path.basename(dir)
    dir = os.path.dirname(dir)
  
  old_name = dir + '\\' + item
  
  item = item.encode('cp850').decode('cp866')       # process item (file or folder name)
  
  new_name = dir + '\\' + item
  os.rename(old_name, new_name)
  return new_name
  
def fix_names(dir):
  flist = os.listdir(dir)           # fix all names in the current dir
  for item in flist:
    fix_name(dir, item)
    
  dlist = get_dirnames(dir)         # enter in each dir and process all its items
  for item in dlist:
    item = dir + '\\' + item
    fix_names(item)
    