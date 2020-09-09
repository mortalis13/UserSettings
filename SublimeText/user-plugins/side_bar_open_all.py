
# Opens all files in selected folder

import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

from .modules.file_system_functions import *


class SideBarOpenAllCommand(sublime_plugin.WindowCommand):
  def run(self, paths = [], recursive = True):
    view_count = 0
    first_view = None
    
    for path in paths:
      if recursive:
        files_list = get_filepaths_in_tree(path)
      else:
        files_list = get_filepaths(path)
      
      for i in range(0, len(files_list)):
        filepath = files_list[i]
        current_view = self.window.open_file(filepath)
        
        if i == 0:
          first_view = current_view
        
    self.window.focus_view(first_view)
    