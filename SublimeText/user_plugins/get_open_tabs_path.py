import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

class GetOpenTabsPathCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # print('get_open_tabs_path')
    
    view = self.view
    views = view.window().views()
    
    res = ''
    
    for v in views:
      file_path = v.file_name()
      res += file_path + '\n'
      
    result_view = view.window().new_file()
    result_view.run_command('insert', {"characters": res})
    