
# Creates files from template replacing variables with values
# new_files_list_file sets the list of files to create

import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

class GenerateFromTemplateCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    out_folder = 'c:/out_folder'
    
    tmpl_file = 'C:/Users/user/AppData/Roaming/Sublime Text 3/Packages/user-templates/java/pojo-tmpl.java'
    new_files_list_file = 'C:/Users/user/AppData/Roaming/Sublime Text 3/Packages/user-templates/java/pojo-files.txt'
    
    tmpl_file = codecs.open(tmpl_file, encoding='utf-8', mode='r')
    new_files_list_file = codecs.open(new_files_list_file, encoding='utf-8', mode='r')
    
    tmpl = tmpl_file.read()
    new_files_list = new_files_list_file.readlines()
    
    tmpl_file.close()
    new_files_list_file.close()
      
    for new_file in new_files_list:
      new_file = new_file.strip()
      
      try:
        file = codecs.open(out_folder + new_file + '.java', encoding='utf-8', mode='w')
        doc = tmpl.replace("ClassName", new_file)
        file.write(doc)
        file.close()
      except:
        msg = "-- Create file Exception:\n{0}\n{1}"
        msg = msg.format(sys.exc_info()[0], sys.exc_info()[1])
        print(msg)
        break
        
    print('finish')
