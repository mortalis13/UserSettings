import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

class FindOpenedFilenameInProjectCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # print('find_opened_filename_in_project')
    view = self.view
    filename = os.path.splitext(os.path.basename(view.file_name()))[0]
    
    sublime.set_clipboard(filename)
    
    view.window().run_command('expand_selection', {'to': 'word'})
    view.window().run_command('show_panel', {'panel': 'find_in_files', 'find_str': filename})
    
    # fv = view.window().get_output_panel('find_in_files')
    # fv.run_command('insert', {"characters": filename})
    