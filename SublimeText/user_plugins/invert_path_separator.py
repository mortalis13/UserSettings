
# Replaces \ with / in windows file/folder paths
# copies the result to the clipboard

import sublime, sublime_plugin

class InvertPathSeparatorCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view=self.view
    r=sublime.Region(0, view.size())

    sel=view.sel()
    sel.add(r)
    
    str=view.substr(r)
    res=str.replace('\\', '/')
    view.replace(edit, r, res)
    sublime.set_clipboard(res)
