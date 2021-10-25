import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys


def to_hex(s):
  lst = []
  for ch in s:
    hv = hex(ord(ch))
    lst.append(hv)
  
  return lst


class GetUnicodeFromSelectionCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # print('get_unicode_from_selection')
    
    view = self.view
    selreg = view.sel()
    
    res = ''
    
    for r in selreg:
      text = view.substr(r)
      text_hex_list = to_hex(text)
      text_hex = ' '.join(text_hex_list)
      res += text + ' - ' + text_hex + '\n'
      
    result_view = view.window().new_file()
    result_view.run_command('insert', {"characters": res})
    