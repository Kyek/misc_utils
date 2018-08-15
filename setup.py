import os
import sys

from setuptools import setup, find_packages

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 5)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write('I only work on python 3, sorry!')
    sys.exit(1)

setup(
    name='python_utils',
    version='0.0.1',
    python_requires='>={}.{}'.format(REQUIRED_PYTHON),
    url='https://github.com/Kyek/python_utils',
    author='Kyek',
    author_email='paris_mendoza@protonmail.com',
    description=('Utils that I use :D'),
    packages=find_packages()
)