
# Opens all files from a folder in Sublime

import sublime, sublime_plugin
import os, re, codecs

from user_modules.file_system_functions import *


class OpenAllFilesCommand(sublime_plugin.WindowCommand):
  def run(self):
    view = self.window.show_input_panel('Folder Path:', '', self.on_done, None, None)
    
  def on_done(self, folder):
    flist = get_filenames_in_tree(folder)
    # for fname in flist:
    #   self.window.open_file(fname)
