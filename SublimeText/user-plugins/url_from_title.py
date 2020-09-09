
# Creates URL from article title
# (replace spaces with dashes)

import sublime, sublime_plugin

class UrlFromTitleCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view=self.view
    r=sublime.Region(0, view.size())

    sel=view.sel()
    sel.add(r)
    view.run_command('lower_case')
    
    str=view.substr(r)
    res=str.replace(' ', '-')
    view.replace(edit, r, res)
