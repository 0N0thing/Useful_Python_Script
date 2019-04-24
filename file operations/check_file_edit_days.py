"""
  function: move target files to a given directory which less than given number
  author: s1mple_zj
  date: 2019-4-24
"""
import os, datetime, shutil

def check_file_latest_edit_date(dirPath, days, desPath):
# get file's edit day and check the difference to the given number
    files = os.scandir(dirPath)
    for f in files:
        if os.path.isfile(os.path.join(dirPath, f)):
            file_path, filename = os.path.split(os.path.join(dirPath, f))
            file_formatted_edit_date = datetime.datetime.fromtimestamp(
                os.path.getmtime(os.path.join(dirPath, f)))
            current_time = datetime.datetime.today()
            difference = current_time - file_formatted_edit_date
            if difference.days < days:
                print('These files you want to move: ')
                print('Filename: ' + filename)
                print('Life: ' + str(difference.days) + 'days')
                shutil.move(os.path.join(dirPath, filename), os.path.join(
                    desPath, filename))
                # os.rename(os.path.join(dirPath, filename), os.path.join(
                #   desPath, filename))
            else:
                print('\n' + filename + ' don\'t need to move.')

src_path = input('Input a source path: ')
difference_days = input('Input a day number that files you want to move: ')
dest_path = input('Input a path you want to move to: ')
check_file_latest_edit_date(src_path, int(difference_days), dest_path)