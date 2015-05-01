
import os

def get_version(path_to_venv):
    lib_path = os.path.join(path_to_venv, 'lib')
    items = os.listdir(lib_path)
    assert len(items) == 1
    python_folder = items[0]
    assert python_folder.startswith('python')
    return python_folder.replace('python', '')

