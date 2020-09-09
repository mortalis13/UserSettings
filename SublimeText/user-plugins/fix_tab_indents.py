
# Sets tab_size to a specified value and converts tabs to spaces
# Try with different tab sizes to fix lines indentation in structured text/code

import sublime, sublime_plugin
import os, re, codecs, subprocess

class FixTabIndentsCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.window().show_input_panel('Tab Size:', '', self.on_done, None, None)
    
    
  def on_done(self, tab_size):
    print('Target tab size: ' + tab_size)
    view = self.view
    
    prev_tab_size = view.settings().get('tab_size')
    view.settings().set('tab_size', tab_size)
    view.run_command('expand_tabs', {"set_translate_tabs": "true"})
    view.settings().set('tab_size', prev_tab_size)
    
    print('\nfinish')
    
