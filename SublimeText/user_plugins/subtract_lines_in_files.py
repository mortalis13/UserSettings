
# Subtracts lines of File2 from File1
# difference = minuend - subtrahend

import sublime, sublime_plugin
import os, re, codecs


class SubtractLinesInFilesCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    minuend_path = 'c:/f1.txt'
    subtrahend_path = 'c:/f2.txt'
    
    minuend_file = codecs.open(minuend_path, encoding='utf-8', mode='r')
    subtrahend_file = codecs.open(subtrahend_path, encoding='utf-8', mode='r')
    
    minuend_lines = minuend_file.readlines()
    subtrahend_lines = subtrahend_file.readlines()
    
    difference_lines = []
    difference_text = ''
    
    for minuend_line in minuend_lines:
      minuend_line = minuend_line.strip()
      if len(minuend_line) != 0:
        unique_line = True
        
        for subtrahend_line in subtrahend_lines:
          subtrahend_line = subtrahend_line.strip()
          if len(subtrahend_line) != 0:
            if minuend_line == subtrahend_line:
              unique_line = False
              break
        
        if unique_line:
          difference_text += minuend_line + '\n'
          
    result_view = view.window().new_file()
    result_view.run_command('insert', {"characters": difference_text})
    
    print('\nfinish')
              