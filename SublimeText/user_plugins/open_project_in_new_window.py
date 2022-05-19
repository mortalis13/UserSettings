
# Opens current project in new window (copies the current window)

import sublime, sublime_plugin
import os, re, codecs, subprocess


class OpenProjectInNewWindowCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    items = []

    executable_path = sublime.executable_path()
    if sublime.platform() == 'osx':
      app_path = executable_path[:executable_path.rfind(".app/")+5]
      executable_path = app_path+"Contents/SharedSupport/bin/subl"

    items.append(executable_path)
    items.append('-n')
    projectPath = self.view.window().project_data()['folders'][0]['path']
    items.append(projectPath)
    
    subprocess.Popen(items)
    