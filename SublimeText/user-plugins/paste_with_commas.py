
# Pastes lines from clipboard as 1 line of values separated by comma

import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

class PasteWithCommasCommand(sublime_plugin.TextCommand):
  def run(self, edit, wrap_quotes=True, new_line=False):
    # print('paste_with_commas')
    
    view = self.view
    
    text = sublime.get_clipboard()
    lines = text.split('\n')
    
    res = ''
    
    print(lines)
    
    for i in range(0, len(lines)):
      line = lines[i].strip()
      if not len(line):
        continue
      
      if wrap_quotes:
        line = '\'' + line + '\''
      
      sep = ', '
      if new_line:
        sep = ',\n'
      if i == len(lines) - 1:
        sep = ''
      
      res += line + sep
      
    view.insert(edit, view.sel()[0].a, res)
