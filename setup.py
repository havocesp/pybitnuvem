#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PyBitnuvem

Bitnuvem exchange API wrapper

 - File: pybitnuvem/setup.py
 - Author: Havocesp <https://github.com/havocesp/PyBitnuvem>
 - Created: 2023-01-17

"""
from setuptools import find_packages, setup

setup(
    name='pybitnuvem',
    version='0.1.0',
    package_dir={'': 'pybitnuvem'},
    packages=find_packages(exclude=['.idea*', 'build*', '*.vs', '*.code', '*.atom', f'{__package__}.egg-info*', 'dist*', 'venv*']),
    url=f'https://github.com/havocesp/{__package__}',
    license='UNLICENSE',
    packages_dir={'': __package__},
    keywords=__keywords__,
    author='havocesp',
    author_email='10012416+havocesp@users.noreply.github.com',
    long_description='Bitnuvem exchange API wrapper',
    description='Bitnuvem exchange API wrapper',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ]
)
