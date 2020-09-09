
# Copies current file folder path

import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

class CopyParentFolderPathCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # print('copy_parent_folder_path')
    
    view = self.view
    file_path = view.file_name()
    folder_path = os.path.dirname(file_path)
    sublime.set_clipboard(folder_path)
    