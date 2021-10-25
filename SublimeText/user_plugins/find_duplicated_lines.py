
# Finds duplicated lines in text

import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

class FindDuplicatedLinesCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # print('find_duplicated_lines')
    
    view = self.view
    r=sublime.Region(0, view.size())
    lines = view.lines(r)
    
    folders_count = 0
    first_line = True
    
    names_list = []
    duplicates = []
    res = ''
    
    for line in lines:
      name = view.substr(line).strip()
      if not len(name) == 0:
        names_list.append(name)
        
    unique_set = set(names_list)
    unique_list = list(unique_set)
    
    for name in unique_list:
      indices = [i for i, x in enumerate(names_list) if x == name]
      if len(indices) >= 2:
        res += name + '\n'
    
    result_view = view.window().new_file()
    result_view.run_command('insert', {"characters": res})
    