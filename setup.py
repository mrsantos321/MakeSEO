#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# Check python version
try:
    from src.info import Info
    from src.support import Support
    INFO = Info().get_info()
    Support(INFO).install()
except Exception as e:
    sys.stdout(e)
    sys.exit()

import setuptools


with open('README.md', 'r') as fh:
    long_description = fh.read()
python_requires = ">={}.{}, <{}.{}"
python_requires = python_requires.format(*(INFO['python_min_version'] +
                                           INFO['python_max_version']))
setuptools.setup(
    name=INFO['package_name'],
    version=INFO['package_version'],
    scripts=[
        f"{INFO['package_name']}.py",
    ],
    entry_points={
        'console_scripts': [
            "{0}={0}:main".format(INFO['package_name']),
        ],
    },
    url=INFO['source'],
    project_urls={
        'Documentation': INFO['documentation'],
        'Source': INFO['source'],
    },
    python_requires=python_requires,
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=INFO['required_packages'],
    author=INFO['author'],
    author_email=INFO['email'],
    description=INFO['description'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    license=INFO['license'],
    keywords=INFO['keywords'],
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ]
)
