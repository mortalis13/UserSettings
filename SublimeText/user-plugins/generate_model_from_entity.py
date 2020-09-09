
import sublime, sublime_plugin
import re
import shutil, stat, errno, sys, traceback

from .modules.general_functions import *
from .modules.file_system_functions import *


MODEL_TEMPLATE = """
package {0};

import java.util.List;
import java.util.Date;

public class {1} {{

{2}
{3}
}}
"""

GETTER_TEMPLATE = """
  public {0} get{1}() {{
    return {2};
  }}
  """

SETTER_TEMPLATE = """
  public void set{0}({1} {2}) {{
    this.{2} = {2};
  }}
  """
  
STANDARD_TYPES = [
  'String', 'Integer', 'Long', 'Double', 'Boolean', 'Date', 'BigDecimal', 'int', 'long', 'double', 'boolean'
]


def generate_getter(field):
  rep_var_decl = '^(\\S+?) (\\S+?) (\\S+?);$'
  
  lines = field.split('\n')
  res = ''
  
  for line in lines:
    line = line.strip()
    
    if line.startswith("private "):
      var_type = regex_search(line, rep_var_decl, 2)
      var_name = regex_search(line, rep_var_decl, 3)
      
      var_name_cased = swap_case_first_letter(var_name)
      
      getter = GETTER_TEMPLATE.format(var_type, var_name_cased, var_name)
      setter = SETTER_TEMPLATE.format(var_name_cased, var_type, var_name, var_name, var_name)
      
      res = getter + setter
      
  return res


class GenerateModelFromEntityCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    
    out_path = 'c:/1-Datos/0/'
    package_name = 'es.gobcantabria.aplicaciones.vivarchi.web.model'
    
    prefixPrivateSize = len(u"private $")
    prefixPublicSize = len(u"public $")
    prefixProtectedSize = len(u"protected $")

    bufferLength = sublime.Region(0, self.view.size())
    bufferContentText = self.view.substr(bufferLength)
    bufferContent = bufferContentText.split("\n")
    
    rep_class = '^public class ([^ {]+)'
    rep_var_decl = '^(\\S+?) (\\S+?) (\\S+?);$'
    
    fields = ''
    getters = ''
    
    for line in bufferContent:
      line = line.strip()
      
      if regex_match(line, rep_class):
        class_name = regex_search(line, rep_class, 1) + 'Model'
      
      if line.startswith("private "):
        var_name = regex_search(line, rep_var_decl, 3)
        var_name_cased = swap_case_first_letter(var_name)
        var_type = regex_search(line, rep_var_decl, 2)
        
        if not var_type in STANDARD_TYPES:
          var_type += 'Model'
      
        field = '  private ' + var_type + ' ' + var_name + ';\n\n'
        getter = generate_getter(field)
      
        fields += field
        getters += getter
        
    fields = fields[:-1]
    class_text = MODEL_TEMPLATE.format(package_name, class_name, fields, getters)
    
    class_path = out_path + class_name + '.java'
    class_file = codecs.open(class_path, 'w', 'utf8')
    class_file.write(class_text)
    class_file.close()
    
    # res = class_text
    # result_view = view.window().new_file()
    # result_view.settings().set('auto_indent', False)
    # result_view.run_command('insert', {"characters": res})
    # result_view.run_command("move_to", {"to": "bof"})
    