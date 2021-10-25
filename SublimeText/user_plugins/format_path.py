
# Replaces \ with \\ in windows file/folder paths
# copies the result to the clipboard

import sublime, sublime_plugin

class FormatPathCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view=self.view
    r=sublime.Region(0, view.size())

    sel=view.sel()
    sel.add(r)
    
    view_content=view.substr(r)
    res=view_content.replace('\\', '\\\\')
    view.replace(edit, r, res)
    sublime.set_clipboard(res)
