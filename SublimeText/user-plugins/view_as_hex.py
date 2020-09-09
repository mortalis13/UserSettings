import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

class ViewAsHexCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # print('view_as_hex')
    view = self.view
    window = view.window()
    
    r = sublime.Region(0, view.size())
    text = view.substr(r)
    
    # sel=view.sel()
    # sel.add(r)
    
    res = ''
    for ch in text:
      hv = hex(ord(ch)).replace('0x', '')
      if len(hv) == 1:
        hv = '0' + hv
      res += hv + ' '
      if hv == '0a':
        res += '\n'
      
    view.replace(edit, r, res)
    