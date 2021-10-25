
# Closes all not saved files without save

import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

class CloseAllNoSaveCommand(sublime_plugin.WindowCommand):
  def run(self):
    # print('close_all_no_save')
    
    force = True
    
    views = self.window.views()
    
    for view in views:
      if force or view.is_dirty():
        view.set_scratch(True)
        view.close()
