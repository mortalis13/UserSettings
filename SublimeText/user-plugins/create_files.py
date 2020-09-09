
# Creates files and puts content

import sublime, sublime_plugin

class CreateFilesCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    folder = 'c:/in'
    ext = '.bat'
    
    names = [
      '0','a','b'
    ]
    
    for name in names:
      try:
        hfile = open(folder + name + ext, 'w')
        text = ''
        
        text += 'echo off\n'
        text += 'cd ..\\out\n'
        text += 'mkdir ' + name + '\n'
        text += 'pause'
        
        hfile.write(text)
      finally:
        hfile.close()
    