import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

class AddSelectionAsideCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # print('add_selection_aside')
    view = self.view
    
    sel = view.sel()
    last_sel = len(sel) - 1
    cur_sel_start = sel[last_sel].a
    
    cur_sel_start += 1
    # r = sublime.Region(cur_sel_start, sel[0].b)
    
    # sel.add(r)
    # sel.add(1)
    sel.add(cur_sel_start)
