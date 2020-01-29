import glob
import os

ONE_KB = 1024


def get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""
    file_list = os.listdir(dirname)
    return sorted([file for file in file_list if os.path.getsize(file) >= size_in_kb])


print(get_files(".", ONE_KB))
