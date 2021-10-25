# put numbers in front of each line
# the input is 2 equal lists,
# the order of items in the second list is used to put
# positional numbers to the lines in the first list

import sublime, sublime_plugin
import re

class ReorderFilenamesCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    r = sublime.Region(0, view.size())
    
    lines = view.lines(r)
    text = ''
    
    list1 = []
    list2 = []
    first = True
    
    for reg in lines:
      line = view.substr(reg).strip()
      if not line:
        first = False
        continue
      if first:
        list1.append(line)
      else:
        list2.append(line)
        
    for i in range(len(list1)):
      line1 = list1[i]
      if line1 not in list2:
        continue
      pos = '{:02}'.format(list2.index(line1) + 1)
      list1[i] = pos + '. ' + line1
    
    for i in range(len(list2)):
      list2[i] = '{:02}'.format(i+1) + '. ' + list2[i]
    
    text = '\n'.join(list1) + '\n\n' + '\n'.join(list2) + '\n'
    view.replace(edit, r, text)
    
    sel_reg = 0
    for line in list1:
      sel_reg += len(line)+1
    
    if sel_reg:
      view.sel().clear()
      view.sel().add(sublime.Region(sel_reg, view.size()))
