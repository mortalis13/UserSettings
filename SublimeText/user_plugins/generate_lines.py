
# Creates lines based on a pattern
# 'arg1 arg2'
# numbers from arg1 to arg2

import sublime, sublime_plugin

# class PrintTextCommand(sublime_plugin.TextCommand):
#   def run(self, edit, text):
#     # self.view.insert(edit, self.view.size(), text)
#     self.view.insert(edit, self.view.sel()[0].a, text)
    
    
class GenerateLinesCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view.window().show_input_panel('Pattern: ', '', self.on_done, None, None)
    
  def on_done(self, pattern):
    args = pattern.split(' ')
    
    res = ''
    prefix = ''
    
    start = int(args[0])
    end = int(args[1])
    step = 1
    
    if len(args) > 2:
      step = int(args[2])
    
    view = self.view
    line_reg = view.line(view.sel()[0])
    line = view.substr(line_reg).strip()
    
    # view.replace(self.edit, line_reg, '')
    
    if len(line) != 0:
      prefix = line
    
    i = start
    while i <= end:
      if i == start:
        res += str(i) + '\n'
      else:
        res += prefix + str(i) + '\n'
      i += step
    
    # res += str(start) + '\n'
    # for i in range(start+1, end+1):
    #   res += prefix + str(i) + '\n'
      
    view.run_command('insert', {"characters": res})
    