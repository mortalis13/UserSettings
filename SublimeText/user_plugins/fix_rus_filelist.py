
# Fixes russian filenames/text from cp850 encoding
# (met this problem when unzipped archives downloaded from Google Drive)
# reads list of broken rus text from a file (save it to utf8)
# and writes correct rus text to another file

import sublime, sublime_plugin
import os, re, codecs


class FixRusFilelistCommand(sublime_plugin.WindowCommand):
  def run(self):
    source_file = "path\\to\\file"
    output_file = "path\\to\\file"
    
    file = open(source_file, 'r')
    text = file.read()
    
    text = text.encode('cp1252').decode('utf8')
    res = text.encode('cp850').decode('cp866')
    res = res.encode('utf8').decode('utf8')
    
    file.close()
    
    file = open(output_file, 'w', encoding='utf8')
    file.write(res)
    file.close()
    
    print('\nfinish')


# read a text file using the specified encoding
def readenc(enc):
  source_file = "path\\to\\file"
  try:
    file = codecs.open(source_file, encoding=enc, mode='r')
    for line in file:
      print(enc + ': ' + line)
  except:
    print('[' + enc + ']')
