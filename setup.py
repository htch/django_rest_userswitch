# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-rest-userswitch',
    version='0.0.1',
    author=u'Pavel K.',
    author_email='belszina@gmail.com',
    packages=find_packages(),
    url='https://github.com/htch/django_rest_userswitch',
    license='None',
    description='Instant user switching widget for django rest framework browsable api',
    long_description=open('README.md').read(),
    zip_safe=False,
    include_package_data=True,
)