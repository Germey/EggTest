import errno
import sys
import os
import glob
import tempfile
import shutil
from os.path import join
from subprocess import check_call


project_folder = './projects/demo1'
project_name = 'hello'


def build_project(project):
    egg = build_egg(project)
    print('Built %(project)s into %(egg)s' % {'egg': egg, 'project': project})
    return egg


_SETUP_PY_TEMPLATE = \
    """# Automatically created
from setuptools import setup, find_packages
setup(
    name='%(project)s',
    version='1.0',
    packages=find_packages(),
)"""


# build Egg
def build_egg(project):
    work_path = os.getcwd()
    print(work_path)
    try:
        project_path = os.path.abspath(join(os.getcwd(), project_folder))
        # project_path = join(path, project)
        print('Project path', project_path)
        os.chdir(project_path)
        # settings = config(project_path, 'settings', 'default')
        create_default_setup_py(project_path, project=project)
        d = tempfile.mkdtemp(prefix="build-")
        o = open(os.path.join(d, "stdout"), "wb")
        e = open(os.path.join(d, "stderr"), "wb")
        retry_on_eintr(check_call, [sys.executable, 'setup.py', 'clean', '-a', 'bdist_egg', '-d', d],
                       stdout=o, stderr=e)
        o.close()
        e.close()
        egg = glob.glob(os.path.join(d, '*.egg'))[0]
        # Delete Origin file
        if find_egg(project_path):
            os.remove(join(project_path, find_egg(project_path)))
        shutil.move(egg, project_path)
        return join(project_path, find_egg(project_path))
    # except Exception as e:
    #     print(e.args)
    finally:
        os.chdir(work_path)


def find_egg(path):
    items = os.listdir(path)
    for name in items:
        if name.endswith(".egg"):
            return name
    return None


def create_default_setup_py(path, **kwargs):
    with open(join(path, 'setup.py'), 'w', encoding='utf-8') as f:
        print(kwargs)
        file = _SETUP_PY_TEMPLATE % kwargs
        f.write(file)


def retry_on_eintr(function, *args, **kw):
    """Run a function and retry it while getting EINTR errors"""
    while True:
        try:
            return function(*args, **kw)
        except IOError as e:
            if e.errno != errno.EINTR:
                raise


if __name__ == '__main__':
    build_project(project_name)
