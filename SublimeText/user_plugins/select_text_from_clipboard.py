
# Selects text from clipboard in the current file text

import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys


class SelectTextFromClipboardCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # print('select_text_from_clipboard')
    
    view = self.view
    sel = view.sel()
    r=sublime.Region(0, view.size())
    lines = view.lines(r)
    
    before_region = sel[0]
    match_found = False
    sel.clear()
    
    text = sublime.get_clipboard()
    cp_lines = text.split()
    for cp_line in cp_lines:
      cp_line = cp_line.strip()
      if not len(cp_line):
        continue
        
      for line_region in lines:
        line_text = view.substr(line_region).strip()
        text_found = line_text.find(cp_line) != -1
        if text_found:
          match_found = True
          sel.add(line_region)
    
    if not match_found:
      sel.add(before_region)
    