#!/usr/bin/env python

from distutils.core import setup

setup(name='SnipPy',
      version='1.0',
      description='Commandline snipping tool in Python',
      author='Koen van Eijk',
      author_email='vaneijk.koen@gmail.com',
      url='https://koenvaneijk.be',
      entry_points = {
        'console_scripts': ['snippy=snippy.command_line:main'],
      },
      packages=['snippy'],
      install_requires=[
          'PyQt5==5.10',
          'Pillow==8.3.2',
      ],
)