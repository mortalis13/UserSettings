
# Indents by one space

import sublime, sublime_plugin

class IndentOneCommand(sublime_plugin.TextCommand):
  def run(self, edit, direction='forward'):
    view = self.view
    
    if direction == 'forward':
      temp_tab_size = view.settings().get('tab_size')
      view.settings().set('tab_size', 1)
      view.run_command('indent')
      view.settings().set('tab_size', temp_tab_size)
      
      # point = view.sel()[0].begin()
      # view.insert(edit, point, ' ')
    else:
      point = view.sel()[0].begin()
      start = view.line(point).begin()
      
      if point == start:
        return
        
      region = sublime.Region(point-1, point)
      view.erase(edit, region)
      
      # view.run_command("left_delete")
      
      # prev = self.view.settings().get('tab_size')
      # self.view.settings().set('tab_size', 1)
      # self.view.run_command('indent')
      # self.view.settings().set('tab_size', prev)
