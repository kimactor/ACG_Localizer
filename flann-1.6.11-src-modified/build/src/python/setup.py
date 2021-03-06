#!/usr/bin/env python

from distutils.core import setup
from os.path import exists, abspath, dirname, join
import os
import sys


def find_path():
    lib_paths = [ os.path.abspath('/home/ar2056/direct_matching_torsten/flann-1.6.11-src-modified/build/lib'), abspath(join(dirname(dirname(sys.argv[0])), '../../../lib')) ]
    possible_libs = ['libflann.so', 'flann.dll', 'libflann.dll', 'libflann.dylib']

    for path in lib_paths:
        for lib in possible_libs:
            if exists(join(path,lib)):
                return path

setup(name='flann',
      version='1.6.11',
      description='Fast Library for Approximate Nearest Neighbors',
      author='Marius Muja',
      author_email='mariusm@cs.ubc.ca',
      license='BSD',
      url='http://www.cs.ubc.ca/~mariusm/flann/',
      packages=['pyflann', 'pyflann.io', 'pyflann.bindings', 'pyflann.util', 'pyflann.lib'],
      package_dir={'pyflann.lib': find_path() },
      package_data={'pyflann.lib': ['libflann.so', 'flann.dll', 'libflann.dll', 'libflann.dylib']}, 
)
