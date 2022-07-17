# Copyright 2014 Jason Heeris, jason.heeris@gmail.com
#
# This file is part of the gammatone toolkit, and is licensed under the 3-clause
# BSD license: https://github.com/detly/gammatone/blob/master/COPYING
from setuptools import setup, find_packages

setup(
    name="Gammatone",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
    ],
    extras_require={
        "plot": ["matplotlib"],
        "test": ["nose", "mock"],
    },
    entry_points={
        "console_scripts": [
            "gammatone = gammatone.plot:main",
        ]
    },
)
