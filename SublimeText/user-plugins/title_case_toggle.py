
# Toggles case of the first letter

import sublime, sublime_plugin

class TitleCaseToggleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
      view = self.view
      
      for s in view.sel():
        if s.empty():
          s = view.word(s)

        txt = view.substr(s)
        txt = txt[0].swapcase() + txt[1:]
        view.replace(edit, s, txt)
  
    
    def find_by_class(self, pt, classes, forward):
        if forward:
            delta = 1
            end_position = self.view.size()
            if pt > end_position:
                pt = end_position
        else:
            delta = -1
            end_position = 0
            if pt < end_position:
                pt = end_position

        while pt != end_position:
            if self.view.classify(pt) & classes != 0:
                return pt
            pt += delta

        return pt
