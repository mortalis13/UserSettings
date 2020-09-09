
import sublime, sublime_plugin
import os, re, codecs, subprocess
import shutil, stat, errno
import operator
import http


def get_selection_lines(self):
  view = self.view
  r = view.sel()[0]
  lines = view.lines(r)
  print(lines)
  
def get_selection_text(self):
  view = self.view
  r = view.sel()[0]
  sel_text = view.substr(r)
  print(sel_text)
  
  
def get_all_text(self):
  view = self.view
  r=sublime.Region(0, view.size())
  text = view.substr(r)
  
  
def search_regexp(self):
  match = re.search(pat, text)
  if match:
    res = match.group(group)
    return res
  
  
def process_long_filenames(self):
  f = '\\\\?\\C:\\tools\\'
  fname = 'name.java'
  
  file_path = f + fname
  if not os.path.exists(f):
    os.makedirs(f)
  hfile = open(file_path, 'w')
  hfile.close()
  
  file_path = f + fname
  os.remove(file_path)
  

def longest_line(self):
  lens = []
  res_dict = {}
  
  view = self.view
  r=sublime.Region(0, view.size())
  lines = view.lines(r)
  
  i = 0
  for line in lines:
    name = view.substr(line).strip()
    if not len(name) == 0:
      item = []
      item.append(name)
      item.append(len(name))
      res_dict[i] = item
      i += 1      
  
  max_len = res_dict[0][1]
  max_id = 0
  for i in res_dict:
    leng = res_dict[i][1]
    if leng > max_len:
      max_len = leng
      max_id = i
  
  print('max:', res_dict[max_id])
  


# add index to duplicated strings 
# each line has 2 parts separated by ' >> '
# [part1_01 >> part2_01]
# [part1_02 >> part2_01] => [part1_02 >> part2_01_1]
def rename_duplicated_lines(self, edit):
  view = self.view
  r=sublime.Region(0, view.size())
  lines = view.lines(r)
  
  folders_count = 0
  first_line = True
  
  names_list = []
  duplicates = []
  res = ''
  
  for line in lines:
    name = view.substr(line).strip()
    if not len(name) == 0:
      part1, part2 = name.split(' >> ')
      names_list.append(part2)
      
      subnum = 0
      
      for item in names_list:
        if part2 == item:
          subnum += 1
      
      if subnum > 1:
        part2 += '_' + str(subnum-1)
      
      parts = part1 + ' >> ' + part2
      res += parts + '\n'
      
  sublime.set_clipboard(res)
  

# move files with replace
# in active view put lines
#   [from_path]
#   [to_path]
#   ...
def replace_files(self, edit):
  view = self.view
  r=sublime.Region(0, view.size())
  lines = view.lines(r)
  
  folders_count = 0
  first_line = True
  
  move_list = []
  move_item = []
  
  names_list = []
  duplicates = []
  res = ''
  
  subline_number = 1
  
  for line in lines:
    name = view.substr(line).strip()
    if not len(name) == 0:
      move_item.append(name)
      
      if subline_number == 1:
        subline_number = 2
      elif subline_number == 2:
        subline_number = 1
        move_list.append(move_item[:])
        move_item.clear()
        
  for move_item in move_list:
    from_file = move_item[0]
    to_file = move_item[1]
    
    if from_file.find('5-temp') == -1:
      from_file = move_item[1]
      to_file = move_item[0]
      
    os.replace(from_file, to_file)
  

# search for duplicates in folder by filesize
def search_duplicates_by_size(self, edit):
  folder = 'c:/folder'
  
  sizes_map = {}
  res = ''
  
  files_list = get_filenames_in_tree(folder)
  
  for file_name in files_list:
    file_size = os.stat(file_name).st_size
    sizes_map[file_name] = file_size
  
  i=0
  sizes_map_len = len(sizes_map)
  files_list = sorted(sizes_map)
  
  for file_name in files_list:
    file_size = sizes_map[file_name]
    
    if i<sizes_map_len:
      for j in range(i+1, len(files_list) - 1):
        file1 = files_list[j]
        file_size1 = sizes_map[file1]
        
        if file_size == file_size1:
          res += 'dup:' + file_name + ' :: ' + file1 + '\n'
    
    i += 1
  
  sublime.set_clipboard(res)


# search for duplicates by filename in 2 folders
def search_duplicates_by_name(self, edit):
  folder1 = 'c:/books'
  folder2 = 'g:/books'
  
  res_file_path1 = 'c:/dup_name_log1.txt'
  res_file_path2 = 'c:/dup_name_log2.txt'
  error_log_path = 'c:/dup_name_error_log.txt'
  log_path = 'c:/dup_name_log.txt'
  
  res_file1 = codecs.open(res_file_path1, encoding='utf-8', mode='w')
  res_file2 = codecs.open(res_file_path2, encoding='utf-8', mode='w')
  error_log = codecs.open(error_log_path, encoding='utf-8', mode='w')
  log_file = codecs.open(log_path, encoding='utf-8', mode='w')
  
  res = ''
  res1 = ''
  res2 = ''
  ext = 'pdf'
  
  files_list1 = get_filepaths_in_tree_ext(folder1, ext)
  files_list2 = get_filepaths_in_tree_ext(folder2, ext)
  
  i = 0
  
  for file_path1 in files_list1:
    file_name1 = os.path.basename(file_path1)
    name1, ext1 = os.path.splitext(file_name1)
    
    for file_path2 in files_list2:
      try:
        file_name2 = os.path.basename(file_path2)
        name2, ext2 = os.path.splitext(file_name2)
        
        if ext1 == ext2:
          pattern = '^.*' + re.escape(name1) + '.*$'
          match = re.search(pattern, name2)
          if match:
            line = file_path1 + ' => ' + file_path2 + '\n'
            res_file1.write(line)
            res_file1.flush()
            
          pattern2 = '^.*' + re.escape(name2) + '.*$'
          match2 = re.search(pattern2, name1)
          if match2:
            line2 = file_path1 + ' <= ' + file_path2 + '\n'
            res_file2.write(line2)
            res_file2.flush()
      except:
        msg = "Search Exception:\n{0}\n{1}\n{2}\n{3}\n{4}\n"
        msg = msg.format(file_name1, file_name2, sys.exc_info()[0], sys.exc_info()[1], sys.exc_info())
        error_log.write(msg)
        error_log.write(traceback.format_exc())
        
        # print(msg)
        # traceback.print_exc()
        return
        
    print('Searched: ' + file_path1)
    # log_file.write('Searched: ' + file_path1 + '\n')
    # i += 1
    # if i == 10:
    #   return
    
  log_file.close()
  error_log.close()
  res_file1.close()
  res_file2.close()
  
  print('\nfinish')


def search_duplicates_by_name_from_list():
  folder2 = 'g:/books'
  
  files1_path = 'c:/dup_name_list_files1.txt'
  
  res_file_path1 = 'c:/dup_name_list_log1.txt'
  res_file_path2 = 'c:/dup_name_list_log2.txt'
  error_log_path = 'c:/dup_name_list_error_log.txt'
  log_path = 'c:/dup_name_list_log.txt'
  
  files1 = codecs.open(files1_path, encoding='utf-8', mode='r')
  file_names1 = files1.readlines()
  files1.close()
  
  res_file1 = codecs.open(res_file_path1, encoding='utf-8', mode='w')
  res_file2 = codecs.open(res_file_path2, encoding='utf-8', mode='w')
  error_log = codecs.open(error_log_path, encoding='utf-8', mode='w')
  log_file = codecs.open(log_path, encoding='utf-8', mode='w')
  
  res = ''
  res1 = ''
  res2 = ''
  ext = 'pdf'
  # ext = 'chm'
  # ext = 'djvu'
  
  files_list2 = get_filepaths_in_tree_ext(folder2, ext)
  
  i = 0
  
  for name1 in file_names1:
    name1 = name1.strip()
    
    for file_path2 in files_list2:
      try:
        file_name2 = os.path.basename(file_path2)
        name2, ext2 = os.path.splitext(file_name2)
        
        pattern = '^' + re.escape(name1) + '.*$'
        match = re.search(pattern, name2)
        
        if match:
          line = name1 + ' => ' + file_path2 + '\n'
          res_file1.write(line)
          res_file1.flush()
      except:
        msg = "Search Exception:\n{0}\n{1}\n{2}\n{3}\n{4}\n"
        msg = msg.format(file_name1, file_name2, sys.exc_info()[0], sys.exc_info()[1], sys.exc_info())
        error_log.write(msg)
        error_log.write(traceback.format_exc())
        return
        
    print('Searched: ' + name1)
    
  log_file.close()
  error_log.close()
  res_file1.close()
  res_file2.close()
  
  print('\nfinish')

  
# move files by extension
def move_files_by_extension(self, edit):
  from_folder = 'c:/from'
  to_folder = 'c:/to'
  
  top_dirs = get_dirnames(from_folder)
  
  for directory in top_dirs:
    subdir = from_folder + '/' + directory
    zip_files = get_filenames_ext(subdir, 'zip')
    for zip_file in zip_files:
      from_name = subdir + '/' + zip_file
      to_name = to_folder + '/' + directory + '/' + zip_file
      
      try:
        os.rename(from_name, to_name)
      except:
        msg = "-- Move file Exception:\n{0}\n{1}"
        msg = msg.format(sys.exc_info()[0], sys.exc_info()[1])
        print(msg)
  

# remove all files/folders in a folder
# removes the read-only flag
def remove_files(self, edit):
  folder = 'c:/removed'
  
  top_dirs = get_dirnames(folder)
  
  for directory in top_dirs:
    git_path = folder + '/' + directory + '/' + '.git'
    if os.path.exists(git_path):
      for root, dirs, files in os.walk(git_path, topdown=False):
        for file in files:
          file_path = root + '/' + file
          os.chmod(file_path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
          os.remove(file_path)
        for dirr in dirs:
          dir_path = root + '/' + dirr
          try:
            os.rmdir(dir_path)
          except:
            temp_files_list, temp_dirs_list = get_full_tree(dir_path)
            print()
            print(exc_info[0])
            print('root:', dir_path)
            print('files:', temp_files_list)
            print('dirs:', temp_dirs_list)
            print()
            continue
          
      os.rmdir(git_path)
      

def count_words_frequency(self):
  view = self.view
  r=sublime.Region(0, view.size())
  lines = view.lines(r)
  
  folders_count = 0
  first_line = True
  
  all_words = []
  res_words = []
  res_counts = {}
  res = ''
  
  for line in lines:
    name = view.substr(line).strip()
    if not len(name) == 0:
      words = name.split(' ')
      all_words.extend(words)
      
  for word in all_words:
    if not word in res_counts:
      res_counts[word] = 1
      
  for word in all_words:
    if word in res_words:
      res_counts[word] += 1
    else:
      res_words.append(word)
  
  sorted_x = sorted(res_counts.items(), key=operator.itemgetter(1))
  sorted_1 = sorted(res_counts, key=res_counts.get)
  
  print(sorted_x)
  print(sorted_1)
  
  for word in sorted_1:
    count = res_counts[word]
    if count > 2:
      res += word + ': ' + str(count) + '\n'
      
  sublime.set_clipboard(res)
      
  
def remove_file_with_long_path(self):
  f = '\\\\?\\C:\\longFolderPath'
  fname = 'longFileName.java'
  
  file_path = f + fname
  os.remove(file_path)


def search_lines_in_file(self, edit):
  main_file_path = 'c:/all_lines.txt'
  search_list_path = 'c:/lines_to_search.txt'
  
  main_file = codecs.open(main_file_path, encoding='utf-8', mode='r')
  search_list_file = codecs.open(search_list_path, encoding='utf-8', mode='r')
  
  main_lines = main_file.readlines()
  search_lines = search_list_file.readlines()
  
  main_file.close()
  search_list_file.close()
  
  res = ''
  found_lines = 0
  
  for search_line in search_lines:
    if search_line in main_lines:
      res += search_line.strip() + '\n'
      found_lines += 1
      
  sublime.set_clipboard(res)

  print('found_lines:', found_lines)


def send_http(self):
  # url = 'http://stackoverflow.com/questions/17178483/how-do-you-send-an-http-get-web-request-in-python'
  # r = requests.get(url)
  # print(r.status_code)
  

  url = 'https://en.wikipedia.org/wiki/Python'
  # conn = http.client.HTTPSConnection("en.wikipedia.org")
  # conn.putrequest("GET", "/wiki/Python")
  
  url = 'http://stackoverflow.com/questions/24243108/multiple-login-in-one-browser'
  conn = http.client.HTTPConnection("stackoverflow.com")
  conn.putrequest("GET", "/questions/24243108/multiple-login-in-one-browser")

  conn.putheader("Accept", "text/html")
  conn.endheaders()
  
  res = conn.getresponse()
  
  print(url, res.status, res.reason)
  # print(res.read())


def replace_multiple_in_view(self, edit):
  replace_map = [
    ['from_1', 'to_1'],
    ['from_2', 'to_2'],
    ['from_3', 'to_3'],
  ]
  
  view=self.view
  r=sublime.Region(0, view.size())
  view_content=view.substr(r)
  
  replNum = 0
  for replace in replace_map:
    view_content = view_content.replace(replace[0], replace[1])
    replNum += 1
    
  print(str(replNum) + ' replacements')
  view.replace(edit, r, view_content)


def replace_multiple_in_files(self):
  file_list = [
    'C:/file1.txt',
    'C:/file1.txt'
  ]
  
  replace_map = [
    ['from_1', 'to_1'],
    ['from_2', 'to_2'],
  ]
  
  replNum = 0
  
  for file_path in file_list:
    try:
      replNum = 0
      
      file = codecs.open(file_path, encoding='utf-8', mode='r')
      doc = file.read()
      file.close()
      
      for replace in replace_map:
        doc = doc.replace(replace[0], replace[1])
        replNum += 1
      
      file = codecs.open(file_path, encoding='utf-8', mode='w')
      file.write(doc)
      file.close()
      
      print('[' + file_path + ']\n' + str(replNum) + ' replacements\n')
    except:
      msg = "-- Replace file Exception:\n{0}\n{1}"
      msg = msg.format(sys.exc_info()[0], sys.exc_info()[1])
      print(msg)


def copy_files_with_new_name(self):
  file_list = [
    'C:/file1.txt',
    'C:/file1.txt'
  ]
  
  replace_map = [
    ['from_1', 'to_1'],
    ['from_2', 'to_2'],
  ]
  
  for file_path in file_list:
    try:
      dir_path = os.path.dirname(file_path)
      file_name = os.path.basename(file_path)
      
      for replace in replace_map:
        file_name = file_name.replace(replace[0], replace[1])
        
      # file_name = file_name.replace(replace_from[0], replace_to[0])
      new_file_path = dir_path + '/' + file_name
      
      shutil.copyfile(file_path, new_file_path)
    except:
      msg = "-- Copy file Exception:\n{0}\n{1}"
      msg = msg.format(sys.exc_info()[0], sys.exc_info()[1])
      print(msg)
