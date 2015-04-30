
import os

def get_version(path_to_venv):
    lib_path = os.path.join(path_to_venv, 'lib')
    return os.listdir(lib_path)[0].replace('python', '')

