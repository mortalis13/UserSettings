
# Shows current file path in the bottom panel

import sublime, sublime_plugin
import os, re, codecs, subprocess

 
class ShowFilePathCommand(sublime_plugin.TextCommand):
  def run(self, edit, forward_separator=True):
    window = sublime.active_window()
    view = self.view
    file_path = view.file_name()
    
    if forward_separator:
      file_path = file_path.replace('\\', '/')
    
    if file_path is not None:
      file_name = os.path.basename(file_path)
      file_extension = os.path.splitext(file_name)[1]
      
      panel_view = window.show_input_panel("", file_path, None, None, None)
      panel_view.sel().clear()
      
      region_begin = panel_view.size() - len(file_name)
      region_end = panel_view.size() - len(file_extension)
      sel_region = sublime.Region(region_begin, region_end)
      
      panel_view.sel().add(sel_region)
    else:
      print("panel_error")
    
