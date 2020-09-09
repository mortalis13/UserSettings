
# Shows a list with projects taken from a text file
# The file contains a list of project paths (path to a folder or to a .sublime-project file)
# Selecting an item from the list the project opens in new window

import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

class ListProjectsCommand(sublime_plugin.WindowCommand):
  def run(self):
    packages_folder = self.window.extract_variables()['packages']
    projects_list_file = packages_folder + '/User/projects_list.lst'
    
    projects_list_file = codecs.open(projects_list_file, encoding='utf-8', mode='r')
    projects_list = projects_list_file.readlines()
    projects_list_file.close()
    
    for i in range(0, len(projects_list)):
      projects_list[i] = projects_list[i].strip()
      
    # projects_list = [
    #   'c:/files.sublime-project',
    #   'C:/projects/projext1',
    # ]
    
    def callback(i):
      project = projects_list[i]
      if i != -1 and project:
        subl_new(project)
        
    self.window.show_quick_panel(projects_list, callback)
    

def subl_new(project):
  subl(["-n", project])

def subl(args=[]):
    # learnt from SideBarEnhancements
    executable_path = sublime.executable_path()
    
    if sublime.platform() == 'osx':
        app_path = executable_path[:executable_path.rfind(".app/") + 5]
        executable_path = app_path + "Contents/SharedSupport/bin/subl"
    subprocess.Popen([executable_path] + args)
    
    if sublime.platform() == "windows":
        def fix_focus():
            window = sublime.active_window()
            view = window.active_view()
            window.run_command('focus_neighboring_group')
            window.focus_view(view)
            
        sublime.set_timeout(fix_focus, 300)
