from setuptools import setup
import re

with open('trellochecklist/__init__.py', 'r') as f:
    version = re.search(r"__version__ = '(.*)'", f.read()).group(1)

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='trellochecklist',
    version=version,
    description='Create Trello Checklists',
    long_desciption=readme,
    author='Robbie Clarken',
    author_email='robbie.clarken@gmail.com',
    license='MIT',
    url='https://github.com/RobbieClarken/trellochecklist',
    packages=['trellochecklist'],
    install_requires=['trolly', 'click'],
    entry_points={'console_scripts': []},
)
