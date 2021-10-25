
# Wraps each line with a HTML link
# use link numer as its title

import sublime, sublime_plugin

class WrapUrlsCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view=self.view
    r=sublime.Region(0, view.size())
    
    lines = view.lines(r)
    i=0
    res=""
    
    for linereg in lines:
      i += 1
      str1 = view.substr(linereg)
      str1 = "<a href='" + str1 + "'>\n  link" + str(i) + "\n</a><br>\n"
      res+=str1
      
    # print(res)
    view.replace(edit, r, res)
    
    # sublime.message_dialog("text")
