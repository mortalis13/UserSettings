
import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys
import http
import operator
from encodings.aliases import aliases

from user_modules.file_system_functions import *
from user_modules.general_functions import *


def title_case_first(text):
  return text[0].upper() + text[1:]

def regex_replace(text, pat, re_repl_func):
  res = re.sub(pat, re_repl_func, text)
  return res

    
class TestActionCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    print('Start Test ...\n')
    
    self.test()
    # self.generate_links_from_titles()
    
    # self.copy_files_with_new_name()
    # self.replace_multiple_in_files()
    # self.replace_multiple_in_view(edit)
    
    print('\nfinish')
  
  
# ----------------------------------------------------
  def test(self):
    view = self.view
    r = sublime.Region(0, view.size())
    lines = view.lines(r)
    
    lines = view.substr(r).split('\n')
    fname = lines[0][0].lower()

    outlines=[]
    s=''
    for line in lines:
      line = line.replace('\n', '')
      if line.lower().find(fname) == 0 and s:
        outlines.append(s)
        s = ''
      s += line
    
    s = 'E:/_TEMP/ru-es_slang/'+fname
    f = codecs.open(s, 'w', 'utf8')
    for line in outlines:
      f.write(line+'\n')
    f.close()
    
    
  def delay_f(self):
    print('delay_f')
  
  def test3(self):
    sublime.set_timeout(self.delay_f, 1000)
    
  def test2(self):
    cmd_pid = ["adb", "shell", "pgrep", "metronomics"]
    proc_pid = subprocess.Popen(cmd_pid, shell=True, stdout=subprocess.PIPE)
    out_pid, err = proc_pid.communicate()
    print(out_pid)
    
