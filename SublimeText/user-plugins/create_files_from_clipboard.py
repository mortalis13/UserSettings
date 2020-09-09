import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

class CreateFilesFromClipboardCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # print('create_files_from_clipboard')
    view = self.view
    
    current_path = os.path.dirname(view.file_name()) + '/'
    
    text = sublime.get_clipboard()
    lines = text.split()
    for line in lines:
      try:
        fp = current_path + line
        if not os.path.exists(fp):
          hfile = open(fp, 'w')
          hfile.close()
      except:
        msg = "-- Create file Exception:\n{0}\n{1}"
        msg = msg.format(sys.exc_info()[0], sys.exc_info()[1])
        print(msg)
        break
        