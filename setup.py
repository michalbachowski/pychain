#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
# monkey patch os.link to force using symlinks
del os.link


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.md').read()

setup(
    name='pychain',
    version='0.1.0',
    description='Chain python functions execution',
    long_description=readme,
    author='Michał Bachowski',
    author_email='michal@bachowski.pl',
    url='https://github.com/michalbachowski/pychain',
    packages=[
        'pychain',
    ],
    package_dir={'pychain': 'pychain'},
    include_package_data=True,
    install_requires=[
    ],
    license="MIT",
    zip_safe=False,
    keywords='pychain',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)
