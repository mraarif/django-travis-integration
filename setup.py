# !/usr/bin/env python

from setuptools import find_packages, setup

import travis_integration

setup(
    name='travis_integration',
    version=travis_integration.__version__,
    description='',
    author='aarif',
    url='',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    packages=find_packages(),
    install_requires=[
        'Django==2.2.18',
        'pytz==2019.1',
        'sqlparse==0.4.4'
    ]
)
