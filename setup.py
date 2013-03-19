#!/usr/bin/env python
import os

from setuptools import find_packages, setup

README = open('README.rst').read()

setup(
    name='cmsplugin-team',
    version=__import__('cmsplugin_team').__version__,
    author='Evgeny Demchenko',
    author_email='evgeny.demchenko@gmail.com',
    url='http://github.com/littlepea/cmsplugin-team',
    description = ('Django CMS plugin to list team members/employees.'),
    long_description = README,
    license = "BSD",
    packages=find_packages(),
    provides=['cmsplugin_team', ],
    include_package_data=True,
    install_requires = [
        'django-sekizai',
        'django-filer',
        'django-editor',
    ],
)
