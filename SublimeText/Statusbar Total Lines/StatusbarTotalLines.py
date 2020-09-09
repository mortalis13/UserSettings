import os

import sublime
import sublime_plugin


class StatusbarTotalLinesCommand(sublime_plugin.EventListener):
  def update_total_lines(self, view):
    r=sublime.Region(0, view.size())
    lines = view.lines(r)
    total_lines = '[Total %d]' % len(lines)
    view.set_status('statusTotalLines', total_lines)


  on_post_save_async = update_total_lines
  on_modified_async = update_total_lines
  on_activated_async = update_total_lines
