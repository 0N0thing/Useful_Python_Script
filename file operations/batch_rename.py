"""
  function: rename/change extension a group of files in a given directory
  author: s1mple_zj
  date: 2019-3-14
"""
import os
import glob

def change_file_extension(filePath, oldPattern, extPattern):
# change file extension
    if not glob.glob(os.path.join(filePath, '*' + oldPattern)):
        print("File extension you want to change is not exist!")
    else:
        for fileName in glob.iglob(os.path.join(filePath, '*' + oldPattern)):
                whole_path, ext = os.path.splitext(fileName)
                newname = fileName.replace(ext, extPattern)
                os.rename(fileName, newname)
        print("Changing file extension done!")

def change_file_name(filePath, title, oldPattern):
# change file name
# pattern: filename.xxx -> new(filename).xxx
    if not glob.glob(os.path.join(filePath, '*' + oldPattern)):
        print("File extension you want to change is not exist!")
    else:
        for fileName in glob.iglob(os.path.join(filePath, '*' + oldPattern)):
            file_name, ext = os.path.splitext(os.path.basename(fileName))
            os.rename(fileName, os.path.join(filePath, title % file_name + ext))
        print("Changing file name done!")

def check_choice():
# check input value
    choice = input("Change file name or change file extension(fn/fe)? ")
    if choice == 'fn':
        filePath = input("Input file path you want to change: ")
        oldPattern = '.' + input("Input extension you want to change: ")
        change_file_name(filePath, 'new(%s)', oldPattern)
    elif choice == 'fe':
        filePath = input("Input file path you want to change: ")
        oldPattern = '.' + input("Input extension you want to change: ")
        extPattern = '.' + input("Input new file extension: ")
        change_file_extension(filePath, oldPattern, extPattern)
    else:
        print("Wrong answer!")
        check_choice()

check_choice()