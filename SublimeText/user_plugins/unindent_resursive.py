
# Unindents multilevel lines
# so that each line has equal relative indentation

import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno, sys

class UnindentResursiveCommand(sublime_plugin.TextCommand):
  def run(self, edit, tabs):
    self.tabs = tabs
    delta = 2
    start_tab_size = 4
    self.app_tab_size = self.view.settings().get('tab_size')
    
    view = self.view
    # view.run_command('expand_selection', {"to": "line"})
    sel_text = view.substr(view.sel()[0])
    
    lines = sel_text.split('\n')
    line_start_indexes = []
    
    # lines = []
    # lines_reg = view.lines(view.sel()[0])
    # for line_reg in lines_reg:
    #   lines.append(view.substr(line_reg))

    # lines = [
    #   '                      <div class="form-group col-md-3">',
    #   '                          <label for="building" class="control-label">',
    #   '                              <s:message code="app.label.building" />',
    #   '                          </label>',
    #   '                          <div class="controls">',
    #   '                              <f:select path="building.id" id="building" cssClass="form-control">',
    #   '                                  <f:option value="" label="${labelSelect}" />',
    #   '                                  <f:options items="${buildingList}" itemValue="id"  itemLabel="name" />',
    #   '                              </f:select>',
    #   '                          </div>',
    #   '                      </div>',
    # ]
    
    
    # for line in lines:
    #   print(line)
    # return
    
    for i in range(0, len(lines)):
      line = lines[i]
      if len(line.strip()) != 0:
        sti = self.get_start_text_index(line)
      else:
        sti = -1
      line_start_indexes.append(sti)
      
    # level1_index = min(line_start_indexes)
    level1_index = min_index(line_start_indexes)
    
    for i in range(0, len(line_start_indexes)):
      sti = line_start_indexes[i]
      # print(sti)
      
      if sti != 0:
        line = lines[i]
        
        lev = (sti - level1_index) / start_tab_size + 1
        lev = int(lev)
        nsti = sti - (sti - lev * delta)
        if tabs:
          nsti = int(nsti / self.app_tab_size)
        lines[i] = line[nsti:]
    
    # print('\n--------------\n')
    # for line in lines:
    #   print(line)
    
    res = '\n'.join(lines)
    view.replace(edit, view.sel()[0], res)
    

  def get_start_text_index(self, text):
    print(self.tabs)
    if self.tabs == True:
      match = re.search('^\t+(\S)', text)
      if match:
        return match.start(1) * self.app_tab_size
    else:
      match = re.search('^ +(\S)', text)
      if match:
        return match.start(1)
      
    

def min_index(indexes):
  mi = 0
  
  for i in indexes:
    if i is not None and i != -1:
      mi = indexes[0]
      break
  
  for i in indexes:
    if i is not None and i != -1 and i < mi:
      mi = i
  
  return mi
