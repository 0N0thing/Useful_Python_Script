
import os

def get_root_file_size(dirPath):
    total_file_size = 0
    file_counts = 0
    files = os.scandir(dirPath)
    for f in files:
        if os.path.isfile(os.path.join(dirPath, f)):
            file_size = os.path.getsize(os.path.join(dirPath, f))
            total_file_size += file_size
            transferred_size = calc_file_size(total_file_size)
            file_counts += 1
        else:
            dir_name, ext = os.path.splitext(os.path.basename(os.path.join(
                dirPath, f)))
            print('\nSubdirectories name: ' + str(dir_name))
            get_root_file_size(os.path.join(dirPath, f))

    print('size: ' + str(transferred_size))

# def root_dir_file_size():



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

test = input('input a path: ')
get_root_file_size(test)