
# Selects heading words from a DSL dictionary by multimple selection
# Searches the nearest headings from the current cursors
# And writes them to the file

import sublime, sublime_plugin
import codecs

class ExtractDSLHeadingsCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view=self.view
    r=sublime.Region(0, view.size())
    cur_lines=view.lines(r)
  
    filename = 'path\\to\\folder'
    file = codecs.open(filename, encoding='utf-8', mode='w+')
  
    print()
    
    for pos in view.sel():
      line = view.rowcol(pos.begin())[0]
      
      found = False
      off = 1
      word = '--'
      point = 0
      
      while not found:
        point = view.text_point(line - off, 0)
        reg = view.full_line(point)
        str = view.substr(reg)

        first_char = str[0]
        code = ord(first_char)

        if(code != 9 and code !=32):
          found = True
          word = str
          
        off+=1
        
      file.write(word)
          
    file.close()
    print('finished')
