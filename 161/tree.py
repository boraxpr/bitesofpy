import os


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    files = []
    dirs = []
    for(dirpath, dirnames, filenames) in os.walk(directory):
        for file in filenames:
            files.append(file)
        for dir in dirnames:
            dirs.append(dir)
    return dirs.__len__(), files.__len__()




# print(count_dirs_and_files('project'))