#!/usr/bin/env python3

from setuptools import setup

setup(
    name="joegit",
    version=1.0,
    packages=["joegit"],
    entry_points={"console_scripts": ["joegit = joegit.cli:main"]},
)
