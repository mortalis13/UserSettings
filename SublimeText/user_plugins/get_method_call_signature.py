
# Prints call method expression based on its definition
# from 'void test_met(String param1, int param2)'
# gets 'test_met(param1, param2)'

import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

from user_modules.general_functions import *


class GetMethodCallSignatureCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    method = view.substr(view.sel()[0])
    
    # method = 'void test_met(String param1, int param2)'
    
    method_name = regex_search(method, ' ?([^ ]+)\(', 1)
    method_params = regex_search(method, '\((.+)\)', 1)
    
    if method_params == None or len(method_params) == 0:
      res = str(method_name) + '()'
    else:
      params_list = re.split(', ?', method_params)
      var_list = []
      for param in params_list:
        param = regex_search(param, '[^ ]+$')
        var_list.append(param)
      
      res = method_name + '(' + ', '.join(var_list) + ')'
    
    r=sublime.Region(0, view.size())
    view.replace(edit, r, res)
    