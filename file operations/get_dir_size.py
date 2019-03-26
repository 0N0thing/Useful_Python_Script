
import os

def get_dir_size(dirPath):
    files = os.scandir(dirPath)
    total_file_size = 0
    file_counts = 0
    for f in files:
        if os.path.isfile(os.path.join(dirPath, f)):
            file_size = os.path.getsize(os.path.join(dirPath, f))
            total_file_size += file_size
            transferred_size = calc_file_size(total_file_size)
            file_counts += 1
        else:
            print(f)
            get_dir_size(os.path.join(dirPath, f))

    print('File number except directory: ' + str(file_counts))
    print(str(transferred_size))

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

test = input("input a path: ")
print("Root directory: " + str(test))
print("\nSubdirectories: ")
get_dir_size(test)