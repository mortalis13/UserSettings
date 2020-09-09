import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

from .modules.general_functions import *


def re_repl_spaces(match):
  return ' '

class ConvertSqlCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # print('convert_sql')
    
    format_sql = True
    # format_sql = False
    
    view = self.view
    
    sel = view.sel()
    for pos in sel:
      sql = view.substr(pos)
      sql = regex_replace(sql, '\s+', ' ')
      
      cols_pat = '\((.+)\) values'
      vals_pat = 'values ?\((.+)\)'
      table_pat = 'insert into ([^ ]+)'
      
      columns_str = regex_search(sql, cols_pat, 1)
      values_str = regex_search(sql, vals_pat, 1)
      table = regex_search(sql, table_pat, 1)
      
      columns = columns_str.split(',')
      values_temp = values_str.split(',')
      values = []
      
      skip_item = False
      
      for i in range(0, len(values_temp)):
        if skip_item:
          skip_item = False
          continue
          
        value = values_temp[i]
        if regex_match(value, '\('):
          skip_item = True
          value += ',' + values_temp[i+1]
        
        values.append(value.strip())
      
      cols_count = len(columns)
      vals_count = len(values)
      
      if cols_count != vals_count:
        print('Columns and values don\'t match')
        return
      
      sql_set = ''
      for i in range(0, cols_count):
        column = columns[i]
        value = values[i]
        set_item = '{}={}'.format(column, value)
        
        sep = ','
        if format_sql:
          sep += '\n'
        if i == cols_count-1:
          sep = ''
        sql_set += set_item + sep
        
      sql_where = ''
      
      # sql_res = 'update %s set %s where %s'%(table,sql_set,sql_where)
      sql_res = 'update {} set {}\nwhere {};'.format(table,sql_set,sql_where)
      res = sql_res
      
      result_view = view.window().new_file()
      result_view.run_command('insert', {"characters": res})
