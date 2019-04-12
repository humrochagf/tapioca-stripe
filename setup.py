#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

from setuptools import find_packages, setup

package = 'tapioca_stripe'

with open('README.md', 'rb') as f:
    readme = f.read().decode('utf-8')

with open(os.path.join(package, '__init__.py'), 'rb') as f:
    init_py = f.read().decode('utf-8')

version = re.search(
    "^__version__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE
).group(1)
author = re.search(
    "^__author__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE
).group(1)
email = re.search(
    "^__email__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE
).group(1)

requirements = [
    'tapioca-wrapper<2',
]
test_requirements = [
]

setup(
    name='tapioca-stripe',
    version=version,
    description='Stripe API wrapper using tapioca',
    long_description=readme,
    long_description_content_type="text/markdown",
    author=author,
    author_email=email,
    url='https://github.com/humrochagf/tapioca-stripe',
    packages=find_packages(),
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='stripe api web tapioca',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
