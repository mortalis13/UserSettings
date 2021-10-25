
# Runs opened Sublime plugin file

import sublime, sublime_plugin
import os, re

class RunCurrentPluginCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    file_path = view.file_name()
    file_name_full = os.path.basename(file_path)
    file_name, file_ext = os.path.splitext(file_name_full)
    
    if file_ext == '.py':
      view.window().run_command(file_name)
      
    # view.window().run_command('show_panel', {"panel": "console", "toggle": False})
    