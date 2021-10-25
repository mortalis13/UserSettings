
# Closes tab without save

import sublime, sublime_plugin

class CloseNoSaveCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.set_scratch(True)
    self.view.close()
