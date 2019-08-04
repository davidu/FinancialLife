#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 21:26:07 2016

@author: martin
"""
try:
    from setuptools import setup
    have_setuptools = True
except ImportError:
    from distutils.core import setup
    have_setuptools = False

skw = dict(
    name='FinancialLife',
    version='0.9.4',
    description='A framework for analysing financial products in personalized contexts',
    author='Martin Pyka',
    author_email='martin.pyka@gmail.com',
    maintainer='Martin Pyka',
    maintainer_email='martin.pyka@gmail.com',
    url='https://github.com/MartinPyka/FinancialLife',
    keywords=["finance", "analysis", "simulation", "loan", "bank"],
    license="Apache License, Version 2.0",
    packages=['FinancialLife',
              'FinancialLife.calendar_help',
      	 	  'FinancialLife.examples',
      	 	  'FinancialLife.financing',
              'FinancialLife.products.germany.lbs',
              'FinancialLife.reports',
              'FinancialLife.tax.germany',
              'FinancialLife.templates.html.standard',
    ],
    package_data={'FinancialLife': ['templates/html/standard/*.html']}
)

if have_setuptools is True:
	skw['install_requires'] = [
		'Jinja2>=2.7.2,<3',
		'matplotlib>=1.3.1,<2',
		'numpy>=1.8.1,<2',
		'pandas>=0.18.1,<1',
		'tabulate>=0.7.5,<1',
        'xlwt>=1.2.0',
	]

setup(**skw)
