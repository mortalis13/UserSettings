import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

class OpenPathDoublecmdCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # print('open_path_doublecmd')
    
    doublecmd_path = 'doublecmd.exe'
    
    view = self.view
    file_path = view.file_name()
    file_path = os.path.normpath(file_path)
    folder_path = os.path.dirname(file_path)
    
    # args = [doublecmd_path, '-C', '-T', folder_path]
    args = [doublecmd_path, '-C', '-T', file_path]
    proc = subprocess.Popen(args)
    
    # print("the commandline is {}".format(proc.args))
    