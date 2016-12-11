from distutils.core import setup
import os
from setuptools import find_packages

long_description = 'Python implementation of MediaWiki API'

setup(
    name='pymediawiki',
    version='1.0.0dev1',
    packages=find_packages(),
    url='https://github.com/abinashmeher999/pymediawiki',
    license='MIT',
    author='djr-jsr',
    author_email='djr.jsr@gmail.com',
    description='Python implementation of MediaWiki API',
    long_description=long_description,
    install_requires=['requests'],
    data_files=[('my_data', ['data/metadata.json'])]
)
