import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

class ShowScopeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # print('show_scope')
    view = self.view
    scope_name = view.scope_name(view.sel()[0].b)
    
    print(scope_name)
    