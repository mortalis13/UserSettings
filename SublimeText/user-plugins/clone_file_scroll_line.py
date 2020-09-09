import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

class CloneFileScrollLineCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # print('clone_file_scroll_line')
    view = self.view
    window = view.window()
    
    row, col = view.rowcol(view.sel()[0].b)
    CloneFileScrollLineCommand.line = row + 1
    CloneFileScrollLineCommand.pos = col + 1
    
    window.run_command('clone_file')

class EventListener(sublime_plugin.EventListener):
  def on_clone_async(self, view):
    view.run_command("goto_line", {"line": CloneFileScrollLineCommand.line} )
