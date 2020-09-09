
# Wraps each line with a HTML link
# use last link chunk (before /) or link number as title

import sublime, sublime_plugin
import re

class WrapUrlsLastnameCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view=self.view
    r=sublime.Region(0, view.size())
    
    lines = view.lines(r)
    i=0
    res=""
    
    for linereg in lines:
      i += 1
      url = view.substr(linereg)
      if len(url) == 0:
        url = "<br>\n\n"
      else:
        link_name = 'link' + str(i)
        
        match = re.search('[^/]+$', url)
        if match:
          link_name = match.group()
          
        url = "<a href=\"" + url + "\">\n  " + link_name + "\n</a><br>\n"
      res += url
      
    # print(res)
    view.replace(edit, r, res)
    
    # sublime.message_dialog("text")
