# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

install_requires = [
    'Flask==0.10.1',
    'Flask-WTF==0.11',
    'future==0.14.3',
    'itsdangerous==0.24',
    'jdcal==1.0',
    'Jinja2==2.7.3',
    'MarkupSafe==0.23',
    'openpyxl==2.2.5',
    'pyexcel==0.1.6',
    'pyexcel-io==0.0.5',
    'pyexcel-xls==0.0.7',
    'texttable==0.8.3',
    'Werkzeug==0.10.4',
    'WTForms==2.0.2',
    'xlrd==0.9.3',
    'xlwt==1.0.0',
    'xlwt-future==0.8.0',
]
setup(
    name="demere",
    version="0.1.0",
    description="A pip package",
    license="Other",
    author="Aashish Karki",
    packages=find_packages(),
    install_requires=install_requires,
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
