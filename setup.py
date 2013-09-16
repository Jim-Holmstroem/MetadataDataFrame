#!/usr/bin/python
# -*- coding: utf8 -*-

from setuptools import setup, find_packages

VERSION = '0.2'

setup(
    name='metadatadataframe',
    packages=find_packages(),
    include_package_data=True,
    version=VERSION,
    zip_safe=False,
    install_requires=[
        'numpy',
        'pandas',
    ],
    author = "Jim Holmström",
    author_email = "jim.holmstroem@gmail.com",
    description = "Adds the possibility to add a metadata"
                  "attribute which gets pickled properply.",
    license = "Free",
    keywords = "pandas dataframe metadata attributes",
    url = "",
)
