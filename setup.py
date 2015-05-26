#!/usr/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.md')).read()

requires = [
    'nose'
]

config = {
    'description': 'Geographic information for Lightbase',
    'long_description': README + '\n\n' + CHANGES,
    'keywords': 'web postgis',
    'author': 'Eduardo F. Santos',
    'url': 'www.lightbase.com.br',
    'download_url': 'http://github.com/lightbase/LBGeo',
    'author_email': 'eduardo@eduardosan.com',
    'version': '0.1',
    'include_package_data': True,
    'zip_safe': False,
    'install_requires': requires,
    'tests_require': requires,
    'packages': find_packages(),
    'scripts': [
    ],
    'test_suite': 'lbgeo',
    'name': 'LBGeo'
}

setup(**config)
