
import os

def get_dir_size(dirPath):
    files = os.scandir(dirPath)
    total_file_size = 0
    file_counts = 0
    dir_count = 0
    for f in files:
        if not os.path.isfile(os.path.join(dirPath, f)):
            dir_name, ext = os.path.splitext(os.path.basename(os.path.join(
                dirPath, f)))
            print('\nSubdirectories name: ' + str(dir_name))
            dir_count += 1
            print(str(dir_count))
            get_dir_size(os.path.join(dirPath, f))
        else:
            file_size = os.path.getsize(os.path.join(dirPath, f))
            total_file_size += file_size
            transferred_size = calc_file_size(total_file_size)
            file_counts += 1


    # print('Counts of files except subdirectories: ' + str(file_counts))
    # print('Directory size: ' + str(transferred_size))
    print('counts: ' + str(file_counts))
    print('size: ' + str(transferred_size))
    return file_counts, transferred_size


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
print('Root directory: ' + str(test))
root_dir_counts,  root_dir_size = get_dir_size(test)
print('Number of root directory files: ' + str(root_dir_counts) +
      '\tRoot directory size:' + str(root_dir_size))

# get_dir_size(test)