
# Generates links within a range

import sublime, sublime_plugin
import os, re, codecs, subprocess

class GenerateLinksCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    
    res = ''
    line = ''
    url = ''
    
    pref = 'prefix'
    suff = '.mp3'
    sep = "<br>\n"

    for i in range(439, 750):
      line = pref + str(i) + suff
      url = '<a href="' + line + '">Link Name ' + str(i) + '</a>'
      res += url + sep
      
    # print(res)
    view.run_command('insert', {"characters": res})
    
    print('---links_finish1---')
    