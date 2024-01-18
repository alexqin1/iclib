#!/usr/bin/env python3

from setuptools import find_packages, setup

setup(
    name='iclib',
    version='0.0.0.dev0',
    description='A collection of integrated circuit libraries in pure Python',
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    url='https://github.com/blueskysolarracing/iclib',
    author='Blue Sky Solar Racing',
    author_email='blueskysolar@studentorg.utoronto.ca',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    keywords=[
        'python',
        'adc78h89',
        'ina229',
        'mcp23s17',
        'mcp4161',
        'sn74hcs137',
        'ti',
        'texas instruments',
        'microchip technology',
    ],
    project_urls={
        'Documentation': 'https://iclib.readthedocs.io/en/latest/',
        'Source': 'https://github.com/blueskysolarracing/iclib',
        'Tracker': 'https://github.com/blueskysolarracing/iclib/issues',
    },
    packages=find_packages(),
    install_requires=['python-periphery>=2.4.0,<3'],
    python_requires='>=3.11',
    package_data={'iclib': ['py.typed']},
)
