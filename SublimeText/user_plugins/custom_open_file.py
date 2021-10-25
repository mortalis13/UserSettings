
# Open a file by its path and goes to a line

import sublime, sublime_plugin
import os

class CustomOpenFileCommand(sublime_plugin.WindowCommand):
  filename = ""
  line = 1
  
  def run(self, file, line):
    # self.window.new_file()

    CustomOpenFileCommand.filename = file
    CustomOpenFileCommand.line = line
    self.window.open_file(file)
    

class EventListener(sublime_plugin.EventListener):
  def on_load_async(self, view):
    current_file_path = view.file_name()
    param_file_path = CustomOpenFileCommand.filename
    
    current_file_path = os.path.normpath(current_file_path)
    param_file_path = os.path.normpath(param_file_path)
    
    if current_file_path == param_file_path:
      view.run_command("goto_line", {"line": CustomOpenFileCommand.line} )
      