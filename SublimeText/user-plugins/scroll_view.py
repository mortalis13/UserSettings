
# Scrolls view without moving the cursor
# -- Generalized function for scroll_ plugins --
# -- (alternative to scroll_lines_fixed third-party plugin)

import sublime, sublime_plugin

class ScrollViewCommand(sublime_plugin.TextCommand):
  def run(self, edit, amount):
    view = self.view
    r = view.visible_region()
    
    view_reg = sublime.Region(0, view.size())
    total_lines = len(view.lines(view_reg))
    
    first_visible_line = view.rowcol(r.a)[0]
    last_visible_line = view.rowcol(r.b)[0]
    
    # down/up
    if amount < 0:
      new_line = last_visible_line - amount
      if new_line > total_lines:
        new_line = total_lines
    else:
      new_line = first_visible_line - amount + 1
      if new_line < 0:
        new_line = 0

    pt = view.text_point(new_line, 0)
    view.show(pt, False)
