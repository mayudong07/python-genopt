from setuptools import setup, find_packages
import os

def readme():
    with open('README.rst') as f:
        return f.read()

requiredpackages = ['numpy', 'matplotlib', 'flame']

setup(
        name     = "genopt",
        version  = "0.0.1",
        description = "General multi-dimensional optimization package",
        long_description = readme() + '\n\n',
        author   = "Tong Zhang",
        author_email = "zhangt@frib.msu.edu",
        platforms = ["Linux"],
        license  = "MIT",
        packages = find_packages(),
        requires = requiredpackages,
)
