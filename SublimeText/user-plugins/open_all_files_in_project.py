
# Opens all files the current project in Sublime

import sublime, sublime_plugin
import os, re, codecs

from user_modules.file_system_functions import *


class OpenAllFilesInProjectCommand(sublime_plugin.WindowCommand):
  def run(self):
    data = self.window.project_data()
    first_folder = data['folders'][0]['path']
    
    if len(first_folder) == 0:
      return
      
    flist = get_filepaths_in_tree(first_folder)
    for file_path in flist:
      self.window.open_file(file_path)
    