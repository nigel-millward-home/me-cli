import os
import shutil
import time


def delete_downloads(days):
    path = '/Users/millwn04/Downloads/'
    now = time.time()

    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if os.path.getmtime(full_path) < now - days * 86400:
            if os.path.isfile(full_path):
                os.remove(full_path)
                print(f'File deleted: {file}')
            elif os.path.isdir(full_path):
                shutil.rmtree(full_path)
                print(f'Path deleted: {file}')
