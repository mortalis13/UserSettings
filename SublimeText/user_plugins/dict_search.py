
# Replaces a text (key) with its value in the dictionary

import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

class DictSearchCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # print('dict_search')
    
    names_dict = dict({
      'key1': 'value1',
    })
    
    view = self.view
    
    sel = view.sel()
    for pos in sel:
      w = view.word(pos)
      key = view.substr(w)
      
      if key in names_dict:
        res = names_dict[key]
        res = ' ' + res
        
        view.insert(edit, pos.a, res)
