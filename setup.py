#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import records
version = records.__version__

setup(
    name='records',
    version=version,
    author='',
    author_email='rebeccashiel@gmail.com',
    packages=[
        'records',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['records/manage.py'],
)
