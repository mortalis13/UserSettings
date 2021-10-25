
# Creates a new Sublime plugin with a name like 'plugin_name'
# Adds a new command to User Commands so the created plugin can be tested
# calling it from the Command Palette by its full name ('Plugin Name')

import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

from user_modules.general_functions import *


class CreatePluginCommand(sublime_plugin.WindowCommand):
  def run(self):
    view = self.window.show_input_panel('Plugin Name: ', '', self.on_done, None, None)
    
    
  def on_done(self, plugin_name):
    plugins_folder = 'user-plugins'
    tmpl_folder = 'user-templates/python'
    
    packages_folder = self.window.extract_variables()['packages']
    plugins_folder = os.path.normpath(packages_folder + '/' + plugins_folder) + '/'
    tmpl_folder = os.path.normpath(packages_folder + '/' + tmpl_folder) + '/'
    
    command_name = plugin_class_name(plugin_name)
    
    repl_map = [
      ['<<command_name>>', command_name],
      ['<<plugin_name>>', plugin_name]
    ]
    
    tmpl_file = codecs.open(tmpl_folder + 'new_plugin_py.tmpl', encoding='utf-8', mode='r')
    tmpl_file = tmpl_file.read()
    
    for repl in repl_map:
      tmpl_file = tmpl_file.replace(repl[0], repl[1])
    text = tmpl_file
    
    plugin_file_name = plugin_name + '.py'
    
    file = codecs.open(plugins_folder + plugin_file_name, encoding='utf-8', mode='w')
    file.write(text)
    file.close()
    
    print('New plugin created: ' + plugin_file_name)
    
    self.window.open_file(plugins_folder + plugin_file_name)
    self.add_command_to_palette(plugin_name)
    
  
  def add_command_to_palette(self, plugin_name):
    packages_folder = self.window.extract_variables()['packages']
    commands_file_path = packages_folder + '/User/Default.sublime-commands'
    
    commands_file = codecs.open(commands_file_path, encoding='utf-8', mode='r')
    commands_text = commands_file.read()
    commands_file.close()
    
    ins_pt = commands_text.index('[') + 1
    
    plugin_caption = plugin_caption_name(plugin_name)
    new_command = '{\n        "command": "' + plugin_name + '",\n        "caption": "' + plugin_caption +  '"\n    },'
    
    commands_text = insert_substring(commands_text, ins_pt, '\n    ' + new_command)
    
    commands_file = codecs.open(commands_file_path, encoding='utf-8', mode='w')
    commands_file.write(commands_text)
    commands_file.close()
  

# --- funcs ---

def rx_repl_class(match):
  return match.group(1).upper()
def rx_repl_caption(match):
  return ' ' + match.group(1).upper()

def plugin_class_name(text):
  pat = '_(.)'
  res = re.sub(pat, rx_repl_class, text)
  res = title_uppercase_first(res)
  return res

def plugin_caption_name(text):
  pat = '_(.)'
  res = re.sub(pat, rx_repl_caption, text)
  res = title_uppercase_first(res)
  return res

def insert_substring(text, index, subtext):
  return text[:index] + subtext + text[index:]

