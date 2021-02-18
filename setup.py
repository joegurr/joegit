#!/usr/bin/env python3

from setuptools import setup

setup(name='vgit',
      version=1.0,
      packages=['vgit'],
      entry_points={
          'console_scripts': [
              'vgit = vgit.cli:main'
          ]
      })
