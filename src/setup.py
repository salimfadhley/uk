#! /usr/bin/env python
from setuptools import setup
import os

PROJECT_ROOT, _ = os.path.split(__file__)
REVISION = '0.0.1'
PROJECT_NAME = 'pythonjob'
PROJECT_AUTHORS = ""
PROJECT_EMAILS = ''
PROJECT_URL = ""
SHORT_DESCRIPTION = 'Statically compiled job board.'

try:
    DESCRIPTION = open(os.path.join(PROJECT_ROOT, "readme.rst")).read()
except IOError:
    DESCRIPTION = SHORT_DESCRIPTION

setup(
    name=PROJECT_NAME.lower(),
    version=REVISION,
    author=PROJECT_AUTHORS,
    author_email=PROJECT_EMAILS,
    packages=['pythonjob', 'pythonjob_tests'],
    zip_safe=True,
    include_package_data=False,
    install_requires=['jekyll'],
    test_suite='nose.collector',
    tests_require=[],
    url=PROJECT_URL,
    description=SHORT_DESCRIPTION,
    long_description=DESCRIPTION,
    license='MIT',
    classifiers=[],
)
