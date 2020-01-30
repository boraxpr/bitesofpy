from glob import glob
import os
import random

ONE_KB = 1024


def get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""
    glob_pattern = os.path.join(dirname, '*')
    return [file for file in glob(glob_pattern) if os.path.getsize(file) >= ONE_KB*size_in_kb]