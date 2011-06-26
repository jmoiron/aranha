#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script for aranha."""

from setuptools import setup, find_packages
import sys, os

from aranha import VERSION
version = '.'.join(map(str, VERSION))

# some trove classifiers:

# License :: OSI Approved :: MIT License
# Intended Audience :: Developers
# Operating System :: POSIX

setup(
    name='aranha',
    version=version,
    description="simple gevent based web spider and tools",
    long_description=open('README.rst').read(),
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
    ],
    keywords='python gevent spider',
    author='Jason Moiron',
    author_email='jmoiron@jmoiron.net',
    url='http://github.com/jmoiron/aranha',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    test_suite="tests",
    install_requires=[
      # -*- Extra requirements: -*-
      'gevent',
      'httplib2',
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,
)
