
# Copies filename

import sublime, sublime_plugin, os, re

class CopyFilenameCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    filename=os.path.basename(self.view.file_name())
    filename=re.sub(r"\.[^\.]+$","",filename)
    # filename=re.sub(r"\..+$","",filename)
    # filename=filename.replace(".txt","")

    sublime.set_clipboard(filename)
