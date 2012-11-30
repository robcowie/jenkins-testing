# -*- coding: utf8 -*-

from os import path
from setuptools import setup, find_packages

requirements = open(path.join(path.dirname(__file__), 'requirements.txt'))\
                .read().strip().split('\n')

setup(
    name="awesome",
    version="0.0.1",
    author="Rob",
    author_email="dev@skimlinks.com",
    description=("Impart awesomeness"),
    packages=find_packages(),
    install_requires=requirements
)
