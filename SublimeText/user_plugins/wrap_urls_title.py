
# Wraps each line with a HTML link
# use previous line as link title
# source text should have the structure:
#   
#   <title>
#   <link>
#   
#   <title>
#   <link>
#   

import sublime, sublime_plugin
import re

class WrapUrlsTitleCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    r = sublime.Region(0, view.size())
    
    lines = view.lines(r)
    res = ""
    item = {}
    url_part = 0
    
    for linereg in lines:
      line = view.substr(linereg)
      
      if url_part == 0:
        if len(line.strip()) == 0:
          continue
        item['title'] = line
        url_part += 1
      elif url_part == 1:
        item['url'] = line
        url_part += 1
      elif url_part == 2:
        url_part = 0
        url = "<a href=\"" + item['url'] + "\">\n  " + item['title'] + "\n</a><br>\n" 
        res += url
        item['title'] = ''
        item['url'] = ''
      
    # print(res)
    view.replace(edit, r, res)
    
    # sublime.message_dialog("text")
