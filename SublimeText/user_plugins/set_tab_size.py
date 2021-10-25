
# Sets tab indent size to 1

import sublime, sublime_plugin

class SetTabSizeCommand(sublime_plugin.TextCommand):
  def run(self, edit, size):
    self.view.settings().set('tab_size', size)
