
# Opens files by path from clipboard

import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

class OpenFilesFromClipboardCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # print('open_files_from_clipboard')
    
    text = sublime.get_clipboard()
    lines = text.split()
    for line in lines:
      if os.path.exists(line):
        self.view.window().open_file(line)
    