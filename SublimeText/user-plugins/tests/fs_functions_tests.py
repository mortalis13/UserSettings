
from user_modules.file_system_functions import *

root_dir = 'c:/user_modules'
ext = 'htm'
exclude_dirs = [
  'backups',
  'read',
  'update-info',
]


def before_test(test_name):
  print('\n** Running test: ' + test_name + ' **')
  
  
def fs_functions_tests():
  print('\n-- fs_functions_tests START')
  
  get_filenames_test()
  
  get_filenames_ext_test()
  
  get_dirnames_test()
  
  get_filenames_in_tree_test()
  
  get_full_tree_test()
  
  get_filepaths_in_tree_test()
  
  get_filepaths_in_tree_ext_test()
  
  get_filepaths_in_tree_filter_dirs_test()
  
  get_filepaths_in_tree_ext_filter_dirs_test()
  
  get_extensions_in_tree_test()
  
  print('\n-- fs_functions_tests END')
  
  
def get_filenames_test():
  before_test('get_filenames')
  res = get_filenames(root_dir)
  print(res)
  
  
def get_filenames_ext_test():
  before_test('get_filenames_ext')
  res = get_filenames_ext(root_dir, ext)
  print(res)
  
  
def get_dirnames_test():
  before_test('get_dirnames')
  res = get_dirnames(root_dir)
  print(res)
  
  
def get_filenames_in_tree_test():
  before_test('get_filenames_in_tree')
  res = get_filenames_in_tree(root_dir)
  print(res)
  
  
def get_full_tree_test():
  before_test('get_full_tree')
  res = get_full_tree(root_dir)
  print(res)
  
  
def get_filepaths_in_tree_test():
  before_test('get_filepaths_in_tree')
  res = get_filepaths_in_tree(root_dir)
  print(res)
  
  
def get_filepaths_in_tree_ext_test():
  before_test('get_filepaths_in_tree_ext')
  res = get_filepaths_in_tree_ext(root_dir, ext)
  print(res)
  
  
def get_filepaths_in_tree_filter_dirs_test():
  before_test('get_filepaths_in_tree_filter_dirs')
  res = get_filepaths_in_tree_filter_dirs(root_dir, exclude_dirs)
  print(res)
  
  
def get_filepaths_in_tree_ext_filter_dirs_test():
  before_test('get_filepaths_in_tree_ext_filter_dirs')
  res = get_filepaths_in_tree_ext_filter_dirs(root_dir, ext, exclude_dirs)
  print(res)
  
  
def get_extensions_in_tree_test():
  before_test('get_extensions_in_tree')
  res = get_extensions_in_tree(root_dir)
  print(res)
