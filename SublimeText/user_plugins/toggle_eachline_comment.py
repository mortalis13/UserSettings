
# Adds/removes comments for each line in selection
# instead of commenting the entire block

import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

class ToggleEachlineCommentCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    r = view.sel()[0]
    lines = view.lines(r)
    
    comment_start = '<!-- '
    comment_end = ' -->'
    
    res = ''
    
    full_text = view.substr(r)
    last_char = full_text[len(full_text)-1]
    # print('last_char(' + str(len(last_char)) + ') ' + last_char)
    
    for line in lines:
      text = view.substr(line)
      res += comment_start + text + comment_end + '\n'
    
    if last_char != '\n':
      res = res[:len(res)-1]
    
    # print('---')
    # print(res)
    # print('---')
    
    view.replace(edit, r, res)
    