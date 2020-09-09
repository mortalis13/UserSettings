
# Subtracts lines using current view (tab) and next tab
# parts are separated by an empty line
# difference = minuend - subtrahend
# `direcion` = [0, 1, 2] => [all, a-b, b-a]

import sublime, sublime_plugin
import os, re, codecs


class SubtractLinesWithNextTabCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    direction = 0
    
    minuend_lines = []
    subtrahend_lines = []
    
    view = self.view
    window = view.window()
    views = window.views()
    
    view_id = window.get_view_index(view)[1]
    if view_id == len(views) - 1:
      print('No next tab')
      return
      
    r = sublime.Region(0, view.size())
    lines = view.lines(r)
    
    next_view = views[view_id + 1]
    r = sublime.Region(0, next_view.size())
    next_lines = next_view.lines(r)
    
    
    for line in lines:
      # text = view.substr(line).strip().lower()
      text = view.substr(line).strip()
      if len(text) != 0:
        minuend_lines.append(text)
    
    for line in next_lines:
      text = next_view.substr(line).strip()
      if len(text) != 0:
        subtrahend_lines.append(text)
    
    
    print(len(minuend_lines))
    print(len(subtrahend_lines))
    
    difference_lines = []
    difference_text = ''
    
    difference_text +='[a-b]\n\n'
    difference_lines = list(set(minuend_lines) - set(subtrahend_lines))
    difference_lines.sort(key=str.lower)
    for difference_line in difference_lines:
      difference_text += difference_line + '\n'
    
    if direction == 0 or direction == 2:
      difference_text += '\n----\n\n[b-a]\n\n'
      difference_lines = list(set(subtrahend_lines) - set(minuend_lines))
      difference_lines.sort(key=str.lower)
      for difference_line in difference_lines:
        difference_text += difference_line + '\n'
      
    
    # for minuend_line in minuend_lines:
    #   minuend_line = minuend_line.strip()
    #   if len(minuend_line) != 0:
    #     unique_line = True
        
    #     for subtrahend_line in subtrahend_lines:
    #       subtrahend_line = subtrahend_line.strip()
    #       if len(subtrahend_line) != 0:
    #         if minuend_line == subtrahend_line:
    #           unique_line = False
    #           break
        
    #     if unique_line:
    #       difference_text += minuend_line + '\n'
          
    result_view = window.new_file()
    result_view.run_command('insert', {"characters": difference_text})
    
    print('\nfinish')
              