
# Toggles vim-like input mode

import sublime, sublime_plugin

class ToggleCommandModeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    s = sublime.load_settings("Preferences.sublime-settings")
    val = s.get('custom_command_mode')
    
    if not val == None:
      print('custom_command_mode: ' + str(val))

      s.set('custom_command_mode', not val)
      # self.view.settings().set('custom_command_mode', not val)
      sublime.save_settings("Preferences.sublime-settings")

      if val == True:
        stat = 'OFF'
      else:
        stat = 'ON'
      sublime.status_message('[' + stat + ']' + ' custom_command_mode ')
