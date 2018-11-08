import sys
from os.path import join
import importlib

# define project path and project name, same as build.py
project_path = './projects/demo1'
project_name = 'hello'
egg_path = 'dist/hello-1.0-py3.6.egg'

# append egg path to system path
sys.path.append(join(project_path, egg_path))

# import module by importlib
module = importlib.import_module(project_name)
# call run() method
module.run()

# import subprocess

# result = subprocess.Popen()