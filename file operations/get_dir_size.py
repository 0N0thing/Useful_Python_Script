"""
  function: output size of a given directory and its subdirectories
  author: s1mple_zj
  date: 2019-4-09
"""
import os

def get_root_file_size(dirPath):
# check file and directory in a given directory, and then, calculate directory
# size
    total_file_size = 0
    files = os.scandir(dirPath)
    for f in files:
        if os.path.isfile(os.path.join(dirPath, f)):
            file_size = os.path.getsize(os.path.join(dirPath, f))
            total_file_size += file_size
            transferred_size = calc_file_size(total_file_size)
        else:
            dir_name, ext = os.path.splitext(os.path.basename(os.path.join(
                dirPath, f)))
            print('\nSubdirectory name: ' + str(dir_name))
            sub_size = get_root_file_size(os.path.join(dirPath, f))
            print('Subdirectory size: ' + str(sub_size))

    return transferred_size

def calc_file_size(size):
# Change file size to a readable format.
    if size < 1024:
        size = str('%.2f' % size) + 'B'
    elif size < 1048576:
        size = str('%.2f' % (size / 1024)) + 'KB'
    elif size < 1073741824:
        size = str('%.2f' % (size / 1048576)) + 'MB'
    else:
        size = str('%.2f' % (size / 1073741824)) + 'GB'
    return size

test = input('Input a target path: ')
print('Root directory name: ' + test)
root_dir_size = get_root_file_size(test)
print('\nRoot directory size(without subdirectories): ' + str(root_dir_size))