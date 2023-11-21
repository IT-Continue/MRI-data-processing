import os
from settings import path_to_raw_data, path_to_output

if not os.path.exists(path_to_reports):
    os.mkdir(path_to_reports)

if not os.path.exists(path_to_recordings):
    os.mkdir(path_to_recordings)