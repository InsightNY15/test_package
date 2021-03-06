#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'numpy==1.9.2'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='test_package',
    version='0.1.0',
    description="A package to tst some tools",
    long_description=readme,
    author="Insight fellows",
    author_email='gautam.sisodia@gmail.com',
    url='https://github.com/InsightNY15/test_package',
    packages=[
        'test_package',
    ],
    package_dir={'test_package':
                 'test_package'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='test_package',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
