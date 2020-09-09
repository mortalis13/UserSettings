
import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

class ReduceIndentCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    # view.run_command('expand_selection', {"to": "line"})
    sel_text = view.substr(view.sel()[0])
    lines = sel_text.split('\n')
    
    # self.test()
    
    res = ''
    for l in lines:
      line_edit = l.strip()
      
      m = re.search(r'^(\s+)', l)
      if m:
        spaces = m.group(0)
        spaces_num = len(spaces)
        line_edit = ' '*(spaces_num//2) + line_edit
      res += line_edit + '\n'
    
    if sel_text[-1] != '\n':
      res = res[:-1]
    
    view.replace(edit, view.sel()[0], res)
    
    
  def test(self):
    lines = [
      '123',
      '    123',
      '        123',
      '            123',
      '                123',
    ]
    
    
    for l in lines:
      line_edit = l.strip()
      
      m = re.search(r'^(\s+)', l)
      if m:
        res = m.group(0)
        spaces_num = len(res)
        
        line_edit = ' '*(spaces_num//2) + line_edit
