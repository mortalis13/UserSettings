
# Copies current line without the newline character

import sublime, sublime_plugin

class CopyLineNofeedCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view=self.view
    r=sublime.Region(0, view.size())

    sel=view.sel()
    line = view.line(sel[0])
    line_contents = view.substr(line)
    
    # print(line_contents)
    sublime.set_clipboard(line_contents)
