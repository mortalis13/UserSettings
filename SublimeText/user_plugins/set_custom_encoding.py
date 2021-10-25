
# Sets custom encoding for the current file

import sublime, sublime_plugin
import os, re, codecs

  
class SetCustomEncodingCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    print(view)
    # view.set_encoding('Cyrillic (Windows 1251)')
    # view.run_command('reopen', {"encoding": "Cyrillic (Windows 1251)"})
    view.window().run_command('reopen', {"encoding": "Hexadecimal"})
    # view.run_command('reopen', "Hexadecimal")
    enc = view.encoding()
    print(enc)
