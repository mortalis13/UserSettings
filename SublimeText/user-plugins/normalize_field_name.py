import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

from .modules.general_functions import *


def re_camel_func(match):
  return match.group(1).upper()

class NormalizeFieldNameCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # print('normalize_field_name')
    
    view = self.view
    # r=sublime.Region(0, view.size())
    # lines = view.lines(r)
    
    sel = view.sel()
    for pos in sel:
      col_name = view.substr(pos).strip()
      var_name = col_name.lower()
      var_name = regex_replace(var_name, '_(.)', re_camel_func)
      var_line = var_name
      
      res = var_line
      view.replace(edit, pos, res)
      
      
      # lines = view.lines(pos)
      # res = ''
      
      # for line in lines:
      #   line_text = view.substr(line).strip()
        
      #   col_name = line_text
      #   var_name = col_name.lower()
      #   var_name = regex_replace(var_name, '_(.)', re_camel_func)
      #   var_line = var_name
        
      #   res += var_line + '\n'
    
      # view.replace(edit, pos, res)
      
    # view.replace(edit, r, res)
    