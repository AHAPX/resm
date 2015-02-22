#!/usr/bin/env python

from setuptools import setup
from pip.req import parse_requirements

setup(
    name = 'pyresm',
    version = '1.0',
    author = 'Anarchy',
    author_email = 'anarchy.b@gmail.com',
    packages = ['pyresm'],
    package_dir = {'pyresm': 'src'},
    data_files = [
        ('/etc', ['conf/resm.conf']),
        ('/usr/local/bin', ['bin/resm']),
        ('/etc/init.d', ['init.d/resm'])
    ],
    install_requires = [
        'flask',
        'flask-restful',
    ],
    test_suite = 'tests'
)
