
# Opens file in Sublime

import sublime, sublime_plugin

class OpenFileByPathCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.window = sublime.active_window()
    panel_view = self.window.show_input_panel("File Path:", "", self.on_done, None, None)
  
  
  def on_done(self, text):
    self.window.open_file(text)
    