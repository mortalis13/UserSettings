import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

class JoinDictLinesRusCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # print('join_dict_lines_rus')
    view = self.view
    r = sublime.Region(0, view.size())
    lines = view.lines(r)
    
    lines = view.substr(r).split('\n')
    fname = lines[0][0].lower()

    outlines=[]
    s=''
    for line in lines:
      line = line.replace('\n', '')
      if line[0].lower() == fname and s:
        outlines.append(s)
        s = ''
      s += line
    if s:
      outlines.append(s)
    
    out_file_name = 'E:/_TEMP/ru-es_slang/'+fname
    f = codecs.open(out_file_name, 'w', 'utf8')
    for line in outlines:
      f.write(line+'\n')
    f.close()
    
    view.window().open_file(out_file_name)
    