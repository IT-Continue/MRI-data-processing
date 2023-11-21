import os
from settings import path_to_raw_data, path_to_output

if not os.path.exists(path_to_raw_data):
    os.mkdir(path_to_raw_data)

if not os.path.exists(path_to_output):
    os.mkdir(path_to_output)