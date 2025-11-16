import os
import time

# Code to update images in the image folder every time the code is run
target = './images/'

def is_file_locked(filepath):
    """Check if a file is locked by attempting to rename it."""
    try:
        os.rename(filepath, filepath)  # Attempt to rename the file
        return False
    except PermissionError:
        return True

def makenew():
    for x in os.listdir(target):
        if x.endswith('.png'):
            file_path = os.path.join(target, x)
            if is_file_locked(file_path):
                print(f"Skipping {file_path} as it is being used by another process.")
            else:
                try:
                    os.unlink(file_path)
                    print(f"Deleted {file_path}.")
                except PermissionError:
                    print(f"Could not delete {file_path}. File is still locked.")
