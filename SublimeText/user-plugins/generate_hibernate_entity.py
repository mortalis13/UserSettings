import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

from .modules.general_functions import *


def re_camel_func(match):
  return match.group(1).upper()


ENTITY_TEMPLATE = """
package {0};

import java.util.List;
import java.util.Date;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.NamedQueries;
import javax.persistence.NamedQuery;
import javax.persistence.Id;
import javax.persistence.Table;
import javax.persistence.ManyToOne;
import javax.persistence.OneToOne;
import javax.persistence.OneToMany;
import javax.persistence.JoinColumn;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.SequenceGenerator;


@Entity
@NamedQueries({{
  @NamedQuery(name = "{1}.findAll", query = "SELECT e FROM {1} e"), 
}})
@Table(name = "{4}")
public class {1} {{
{2}
{3}
}}
"""

FIELD_TEMPLATE = """
  @Column(name = "{0}")
  private {1} {2};
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


TYPES_MAP = {
  'NUMBER': 'Integer',
  'VARCHAR': 'String',
  'VARCHAR2': 'String',
  'DATE': 'Date',
}


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


class GenerateHibernateEntityCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # print('generate_hibernate_entity')
    
    view = self.view
    
    # cols_fp = 'c:/1-Datos/Docs/6-tareas/vivarchi/db/cols.txt'
    cols_fp = 'c:/1-Datos/Docs/6-tareas/vivarchi/db/cols-2.txt'
    out_path = 'c:/1-Datos/0/'
    package_name = 'es.gobcantabria.aplicaciones.vivarchi.business.domain'

    indent_spaces = '  '
    # DEBUG = True
    DEBUG = False
    
    fcols = codecs.open(cols_fp, 'r', 'utf8')
    cols = fcols.readlines()
    
    entities_map = {}
    
    for col in cols:
      col = col.strip()
      if len(col) == 0:
        continue
        
      col_items = re.compile(' +').split(col)
      
      entity_name = col_items[0]
      col_name = col_items[1]
      col_type = col_items[2]
      
      if not entity_name in entities_map:
        entities_map[entity_name] = []
      entities_map[entity_name].append({'col_name': col_name, 'col_type': col_type})
    
    # ---------------------------------
    
    res = ''
    
    for entity_name in entities_map:
      class_name = entity_name.title()
      class_name = regex_replace(class_name, '_(.)', re_camel_func)
      
      cols = entities_map[entity_name]
      cols_count = len(cols)
      fields = indent_spaces + '\n'
      getters = ''
      
      for i in range(0, cols_count):
        col = cols[i]
        col_name = col['col_name']
        col_type = col['col_type']
        
        var_name = col_name.lower()
        var_name = regex_replace(var_name, '_(.)', re_camel_func)
        
        col_java_type = 'String'
        for key in TYPES_MAP:
          if col_type.find(key) != -1:
            col_java_type = TYPES_MAP[key]
          
        # if col_type in TYPES_MAP:
        #   col_java_type = TYPES_MAP[col_type]
          
        field = FIELD_TEMPLATE.format(col_name, col_java_type, var_name)
        getter = generate_getter(field)
        
        fields += field[1:]
        getters += getter[1:]
        
        if i != cols_count-1:
          fields += '\n'
          getters += '\n'
          
      entity_text = ENTITY_TEMPLATE.format(package_name, class_name, fields, getters, entity_name)
      
      
      if DEBUG:
        res += entity_text + '\n\n'
      else:
        class_path = out_path + class_name + '.java'
        class_file = codecs.open(class_path, 'w', 'utf8')
        class_file.write(entity_text)
        class_file.close()
      
    if DEBUG:
      result_view = view.window().new_file()
      result_view.settings().set('auto_indent', False)
      result_view.run_command('insert', {"characters": res})
      result_view.run_command("move_to", {"to": "bof"})
          