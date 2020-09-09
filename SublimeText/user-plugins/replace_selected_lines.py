
# Replaces text in selected lines

import sublime, sublime_plugin

class ReplaceSelectedLinesCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    selreg = view.sel()
    
    for r in selreg:
      line = view.line(r)
      text = view.substr(line)

      text = text.replace('(', '\(')
      text = text.replace(')', '\)')

      view.replace(edit, line, text)
