
# Shows TortoiseSVN log for current file

import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

class ShowLogTortoiseSvnCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # print('show_log_tortoise_svn')
    
    view = self.view
    file_path = view.file_name()
    file_path = os.path.normpath(file_path)
    
    args = ['TortoiseProc', '/command:log', '/path:' + file_path]
    proc = subprocess.Popen(args)
    
    # print("the commandline is {}".format(proc.args))
