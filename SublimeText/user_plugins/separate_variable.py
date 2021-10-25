
# Separates variable declaration from its usage

import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

from user_modules.general_functions import *


class SeparateVariableCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # print('separate_variable')
    
    view = self.view
    r = view.sel()[0]
    sel_text = view.substr(r)
    
    add_init = ''
    # add_init = ' = null'
    
    var_decl = regex_search(sel_text, '^\S+ \S+') + add_init + ';'
    var_impl = regex_search(sel_text, '^\S+ (.+$)', 1)
    
    line_r = view.line(r)
    
    add_spaces = view.substr(sublime.Region(line_r.a, r.a))
    
    res = var_decl + '\n' + add_spaces + var_impl
    # print(res)
    view.replace(edit, r, res)
    
    old_sel = view.sel()[0].b
    view.sel().clear()
    view.sel().add(old_sel)
    