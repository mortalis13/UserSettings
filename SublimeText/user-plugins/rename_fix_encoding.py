
# Fixes encoding for file names and renames them

import sublime, sublime_plugin
import os

from user_modules.file_system_functions import *


class RenameFixEncodingCommand(sublime_plugin.WindowCommand):
  def run(self):
    view = self.window.show_input_panel('Folder Path:', '', self.on_done, None, None)
    self.from_enc = 'latin1'
    self.to_enc = 'utf8'
  
  
  def on_done(self, folder):
    print('\nTrying to fix encoding in folder: ' + folder)
    
    files_list = get_filenames_in_tree(folder)
    
    for file_path in files_list:
      file_name = os.path.basename(file_path)
      file_name = file_name.encode(self.from_enc).decode(self.to_enc)
      
      from_name = file_path
      to_name = os.path.dirname(file_path) + '/' + file_name
      
      try:
        os.rename(from_name, to_name)
      except:
        msg = "-- Rename file Exception:\n{0}\n{1}"
        msg = msg.format(sys.exc_info()[0], sys.exc_info()[1])
        print(msg)
    
    print('\nfinish')
    