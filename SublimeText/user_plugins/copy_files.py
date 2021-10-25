
# Copies files from one folder to another

import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

class CopyFilesCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # print('copy_files')
    # view = self.view.window().show_input_panel('Folder: ', '', self.on_done, None, None)
    
    fsrc = [
      'C:/from1',
      'C:/from2'
    ]
    fdest = 'c:/to'
    self.on_done(fsrc, fdest)
    
    
  def copy_files(folder_src, folder_dest):
    ignore = shutil.ignore_patterns('.svn', 'target', '.metadata')
    shutil.copytree(folder_src, folder_dest, ignore=ignore)
  
  
  def on_done(self, folder_src, folder_dest):
    for fsrc in folder_src:
      dest_folder_name = os.path.basename(fsrc)
      fdest = folder_dest + '/' + dest_folder_name
      
      fsrc = os.path.normpath(fsrc)
      fdest = os.path.normpath(fdest)
      
      fdest = '\\\\?\\' + fdest
    
      self.copy_files(fsrc, fdest)
