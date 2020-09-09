
# Creates Java getters and setters based on list of variables

import sublime, sublime_plugin
import re
import shutil, stat, errno, sys, traceback

from .modules.general_functions import *
from .modules.file_system_functions import *


setterTemplate = """
public void set%s(%s %s) {
  this.%s = %s;
}
"""

getterTemplate = """
public %s get%s() {
  return %s;
}
"""

class GenerateJavaGettersCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    
    # use_tabs = True
    use_tabs = False
    tab_size = 2
    
    prefixPrivateSize = len(u"private $")
    prefixPublicSize = len(u"public $")
    prefixProtectedSize = len(u"protected $")

    bufferLength = sublime.Region(0, self.view.size())
    bufferContentText = self.view.substr(bufferLength)
    bufferContent = bufferContentText.split("\n")
    
    rep_class = '\\bclass\\b'
    rep_var_decl = '^(\\S+?) (\\S+?) (\\S+?);$'
    
    # print(view.substr(view.line(view.sel()[0])))
    
    cursor_start_point = view.sel()[0].a
    line_start_point = view.line(view.sel()[0]).a
    chars_before_cursor = cursor_start_point - line_start_point
    
    if use_tabs:
      chars_before_cursor = chars_before_cursor * tab_size
    
    output = ''
    first_pass = True
    
    for line in bufferContent:
      line = line.strip()
      
      try:
        if regex_match(line, rep_class):
          continue
        
        if line.startswith("private "):
          var_name = regex_search(line, rep_var_decl, 3)
          var_name_cased = swap_case_first_letter(var_name)
          var_type = regex_search(line, rep_var_decl, 2)
          
          # print(var_name)
          # print(var_type)
          
          setTemplate = setterTemplate % (var_name_cased, var_type, var_name, var_name, var_name)
          getTemplate = getterTemplate % (var_type, var_name_cased, var_name)
          

          setTemplateLines = setTemplate.split('\n')
          setTemplate = ''
          line_index = 0
          
          for temp_line in setTemplateLines:
            if line_index == 0:
              line_index += 1
              continue
              
            if first_pass and line_index == 1:
              first_pass = False
            else:
              temp_line = ' ' * chars_before_cursor + temp_line
            
            setTemplate += temp_line + '\n'
            line_index += 1
          
          
          getTemplateLines = getTemplate.split('\n')
          getTemplate = ''
          line_index = 0
          
          for temp_line in getTemplateLines:
            if line_index == 0:
              line_index += 1
              continue
              
            if first_pass and line_index == 1:
              first_pass = False
            else:
              temp_line = ' ' * chars_before_cursor + temp_line
            
            getTemplate += temp_line + '\n'
            line_index += 1
            
          
          if bufferContentText.find('set' + var_name_cased) == -1:
            output += setTemplate
          
          if bufferContentText.find('get' + var_name_cased) == -1:
            output += getTemplate
            
          if(use_tabs):
            output = output.replace('  ', '\t')
          
          
          # print(setTemplate)
          # print(getTemplate)
          
          # cursor_start_point = view.sel()[0].a
          # line_start_point = view.line(view.sel()[0]).a
          # chars_before_cursor = cursor_start_point - line_start_point
          
          # view.insert(edit, self.view.sel()[0].a, setTemplate)
          # view.insert(edit, self.view.sel()[0].a, getTemplate)
        
      except:
        msg = "\n-- Generate getter/setter Exception:"
        print(msg + '\n' + line)
        traceback.print_exc()
        
    view.insert(edit, self.view.sel()[0].a, output.strip())
