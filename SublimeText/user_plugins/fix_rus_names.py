
# Fixes russian filenames/text from cp850 encoding
# (met this problem when unzipped archives downloaded from Google Drive)
# gets text from the current ST view, fixes it and puts the result to the clipboard

import sublime, sublime_plugin
import os, re, codecs

class FixRusNamesCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    r = sublime.Region(0, view.size())

    sel = view.sel()
    sel.add(r)
    
    str = view.substr(r)
    # res = str.encode('cp850').decode('cp866')
    # res = str.encode('cp1252').decode('cp1251')
    res = str.encode('cp1252').decode('cp1251').encode('utf8').decode('utf8')
    view.replace(edit, r, res)
    # sublime.set_clipboard(res)
    
    sel.clear()
    sel.add(0)
