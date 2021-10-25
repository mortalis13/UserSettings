
# Rremoves files by path

import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

from user_modules.file_system_functions import *


class RemoveFilesCommand(sublime_plugin.WindowCommand):
  def run(self):
    # print('remove_files')
    view = self.window.show_input_panel('Path: ', '', self.on_done, None, None)
    
    
  def on_done(self, remove_path):
    res = remove_files(remove_path, True)
    # self.view.window().run_command('show_panel', {"panel": "console", "toggle": False})
    
