
# Removes lines from the current file using the lines from an external file
# Usefull for one-line words/expressions

import sublime, sublime_plugin
import codecs

class SubtractWordFromFileCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view=self.view
    r=sublime.Region(0, view.size())
    cur_lines=view.lines(r)
    
    filename = 'full\\path\\to\\file'
    
    file = codecs.open(filename, encoding='utf-8')
    lines = file.readlines()
    
    replaced = 0
    zero_len = 0
    total = len(lines)
    
    print()
    
    for line in lines:
      line = line.strip()
      if len(line) == 0:
        zero_len+=1
        continue
        
      pos = view.find('^'+line+'$', 0)
      
      if pos.a != -1:
        pos = view.full_line(pos)
        view.replace(edit, pos, '')
        replaced+=1
        
    file.close()
    print('finished, replaced: {} of {}, 0-len: {}'.format(replaced, total, zero_len))
    