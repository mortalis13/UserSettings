
# Moves files to new folders with the same names as files
# 'c:/document1.pdf' to 'c:/document1/document1.pdf'
    
import sublime, sublime_plugin
import os, re, sys

from .modules.file_system_functions import *


class MoveFilesToNewFolderCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    print('\n== Moving Files')
    
    folder = 'c:/dir'
    
    file_type = "pdf"
    
    const_list = [
      'subdir1',
      'subdir2'
    ]
    
    subfolders_level = 1
    
    if not subfolders_level == 0:
      self.move_file_in_subfolder(folder, file_type)
      
      dirlist = get_dirnames(folder)
      dirlist = const_list
      
      for directory in dirlist:
        directory = folder + '/' + directory
        self.move_file_in_subfolder(directory, file_type)
    else:
      self.move_file_in_subfolder(folder, file_type)
    
    print("\n== Files moved")
    
    
  def move_file_in_subfolder(self, folder, ext):
    flist = get_filenames_ext(folder, ext)
    # flist = get_filenames(folder)
    # print(flist)
    
    for fname in flist:
      file_name, file_ext = os.path.splitext(fname)
      folder_full_path = folder + '/' + file_name
      
      try:
        if not os.path.exists(folder_full_path):
          os.mkdir(folder_full_path)
      except:
        print("Create dir Exception:", folder_full_path)
        continue
    
    for fname in flist:
      file_name, file_ext = os.path.splitext(fname)
      folder_full_path = folder + '/' + file_name
      
      from_name = folder + '/' + fname
      to_name = folder_full_path + '/' + fname
      
      try:
        os.rename(from_name, to_name)
      except:
        msg = "-- Move file Exception:\n{0}\n{1}\n{2}\n{3} \n=> {4}"
        msg = msg.format(fname, sys.exc_info()[0], sys.exc_info()[1], from_name, to_name)
        print(msg)
        continue
        