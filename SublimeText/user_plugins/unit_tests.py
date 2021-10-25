
# Tests modules

import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

from .tests.fs_functions_tests import *


class UnitTestsCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # print('unit_tests')
    print('\n=================\n-- UnitTests START')
    
    fs_functions_tests()
  
    print('\n-- UnitTests END\n=================\n')
    
