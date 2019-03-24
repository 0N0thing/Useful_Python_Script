"""
  function: display file's information in a given directory
  author: s1mple_zj
  date: 2019-3-21
"""
import os
import time

def get_file_info(filePath):
# get file name, fullpath and other properties use os.path
    files = os.listdir(filePath)
    for f in files:
        filename, ext = os.path.splitext(os.path.basename(filePath + f))
        ext = ext.split('.')[-1]
        info = os.path.getsize(filePath + f)
        if info < 1024:
            info = str(info) + 'B'
        elif info >= 1024 & info < 1048576:
            info = str(info / 1024) + 'KB'
        elif info >= 1048576 & info < 1073741824:
            info = str(info / 1048576) + 'MB'
        else:
            info = str(info / 1073741824) + 'GB'
        print('full path: ' + filePath + f + '\nfile name: ' + filename
              + '\nextension: ' + ext +'\nfile size: ' + info)
        print('create date: %s' % time.ctime(os.path.getctime(filePath + f)))
        print('last modified date: %s' % time.ctime(os.path.getmtime(filePath
                                                                     + f)) + '\n')

directory = input("Please input a directory which you want to check: ")
get_file_info(directory + '\\')
