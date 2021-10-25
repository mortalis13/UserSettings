
# Replaces \ with \\ in windows file/folder paths
# copies the result to the clipboard

import sublime, sublime_plugin

class FormatAndroidUrlCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view=self.view
    r=sublime.Region(0, view.size())

    sel=view.sel()
    sel.add(r)
    
    str=view.substr(r)
    
    from_str = 'http://developer.android.com/intl/es/'
    to_str = 'file:///g:/android-docs/'
    res=str.replace(from_str, to_str)
    
    view.replace(edit, r, res)
    sublime.set_clipboard(res)
