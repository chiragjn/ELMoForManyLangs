#!/usr/bin/env python
import setuptools


setuptools.setup(
  name="elmoformanylangs",
  version="0.0.2",
  packages=setuptools.find_packages(),
  install_requires=[
    "torch==1.1.0",
    "h5py==2.9.0",
    "numpy==1.16.4",
    "overrides",
  ],
  classifiers=[
    "Development Status :: 2 - Pre-Alpha",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.6",
  ],
)
