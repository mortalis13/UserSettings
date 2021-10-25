import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

class RemoveOpenedFilesCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # print('remove_opened_files')
    view = self.view
    window = view.window()
    
    views = window.views()
    fpaths = []
    for v in views:
      filepath = v.file_name()
      fpaths.append(filepath)
    
    window.run_command('close_all')
    
    for fp in fpaths:
      print('Removing: ' + str(fp))
      os.remove(fp)
    