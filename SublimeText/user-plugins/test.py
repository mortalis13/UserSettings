
import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys
import http
import operator
from encodings.aliases import aliases

from .modules.file_system_functions import *
from .modules.general_functions import *


def title_case_first(text):
  return text[0].upper() + text[1:]

def regex_replace(text, pat, re_repl_func):
  res = re.sub(pat, re_repl_func, text)
  return res

class TestCommand(sublime_plugin.TextCommand):
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
    def rf(match):
      return match.group(1).upper()
    
    res = regex_replace('num_orden', '_(.)', rf)
    print(res)
    
