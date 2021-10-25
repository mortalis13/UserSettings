
# Replaces a string in all files in a folder

import sublime, sublime_plugin
import os, re, codecs
import shutil, stat, errno, sys, ssl

from user_modules.file_system_functions import *


class ReplaceStringInFilesCommand(sublime_plugin.WindowCommand):
  def run(self):
    src_dir = "c:/dir"
    ext = ''
    src_str = "org.apache.commons.logging.Log"
    dest_str = "org.slf4j.Logger"
    
    exclude_dirs = [
      '.svn',
      'target'
    ]
    
    fp_error_log = 'e:/Documents/5-temp/logs/replace_error.log'
    f_error_log = codecs.open(fp_error_log, 'w', 'utf-8')
    
    replaced = 0
    
    if len(ext) == 0:
      flist = get_filepaths_in_tree_filter_dirs(src_dir, exclude_dirs)
    else:
      flist = get_filepaths_in_tree_ext_filter_dirs(src_dir, ext, exclude_dirs)
    
    for file_path in flist:
      try:
        res = replace_in_file(file_path, src_str, dest_str)
        if res:
          replaced += 1
      except:
        msg = "-- Replace Exception: {0}\n{1}\n{2}"
        msg = msg.format(file_path, sys.exc_info()[0], sys.exc_info()[1])
        print('\n' + msg + '\n')
        f_error_log.write(msg + '\n')
        f_error_log.flush()
    
    total = len(flist)
    
    print('\nFinish. Replaced ' + str(replaced) + '/' + str(total))


def replace_in_file(file_path, src_str, dest_str):
  file = codecs.open(file_path, encoding='utf-8', mode='r')
  doc = file.read()
  res = doc.replace(src_str, dest_str)
  file.close()
  
  file = codecs.open(file_path, encoding='utf-8', mode='w')
  file.write(res)
  file.close()
  
  if res == doc:
    return False
  return True
