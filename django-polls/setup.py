# -*- coding: utf-8 -*-
"""
@Time    : 2018-08-30 16:15
@Author  : DukeMoon
"""
import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-tutorials-polls',  # 决定这个包名 $ pip install django-tutorials-polls
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',  # example license
    description='A simple Django app to conduct Web-based polls.',
    long_description=README,
    url='https://www.fake-example.com/',
    author='DukeMoon',
    author_email='dukemoon@qq.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django :: 2.0',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
