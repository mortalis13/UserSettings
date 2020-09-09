import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys
import datetime, time

class ConvertTimeIntervalsCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # print('convert_time_intervals')
    view = self.view
    window = view.window()
    
    r=sublime.Region(0, view.size())
    lines = view.lines(r)
    
    time_format = '%H:%M:%S'
    from_time = '00:00:00'
    
    durations = []
    
    for line in lines:
      line = view.substr(line).strip()
      if len(line.split(':')) == 2:
        line = '00:' + line
      
      d = datetime.datetime.strptime(line, time_format) - datetime.datetime.strptime(from_time, time_format)
      d_str = time.strftime(time_format, time.gmtime(d.total_seconds()))
      res_duration = d_str + '\n'
      
      view.run_command('insert', {"characters": res_duration})
      
      from_time = line
