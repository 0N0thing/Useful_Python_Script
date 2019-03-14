"""
  function: check a directory exist in a given directory, if not, create this
  sub-directory
  author: s1mple_zj
  date: 2019-3-14
"""
import os

def check_directory(dir, dirname):
# check name exist in given directory, if not, create directory
    if not os.path.isdir(os.path.join(dir, dirname)):
        print("Dir not exist, create it!")
        os.makedirs(os.path.join(dir, dirname))
    else:
        print("Directory exist!")

dir = input("Input directory you want to check: ")
dir_name = input("Input a name you want to create: ")
check_directory(dir, dir_name)