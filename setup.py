import os
import sys

from setuptools import setup, find_packages

version = '0.0.2'

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 5)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write('I only work on python 3, sorry!')
    sys.exit(1)

setup(
    name='misc_utils',
    version=version,
    long_description="""\
Seriously, it is just a test; I will add some functions but will be only for my use. Be free to contribute""",
    python_requires='>={}.{}'.format(*REQUIRED_PYTHON),
    license='MIT',
    url='https://github.com/Kyek/misc_utils',
    author='Kyek',
    include_package_data=True,
    author_email='paris_mendoza@protonmail.com',
    description=('Utils that I use :D'),
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
)
