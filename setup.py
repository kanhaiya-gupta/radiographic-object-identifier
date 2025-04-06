"""
Setuptools based setup module
"""
from setuptools import setup, find_packages
import versioneer

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='radiographic_identifier',
    version=versioneer.get_version(),
    description='create a unique digital identifier of additively manufactured components and authenticate the components afterward.',
    long_description='http://radiographic-identifier.org',

    url='https://git.bam.de/kgupta/radiographic_identifier',
    author='Bundesanstalt für Materialforschung und -prüfung - Kanhaiya Gupta',
    author_email='kanhaiya.gupta@bam.de',
    license='Microsoft Reciprocal License (Ms-RL)',

    classifiers=[
        'Development Status :: 1 - Production/Beta',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Science/Research/Industry',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12'
    ],

    keywords='authentication',
    packages=find_packages(exclude=["*tests*", "*docs*", "*binder*", "*conda*", "*notebooks*"]),
    install_requires=requirements,
    cmdclass=versioneer.get_cmdclass(),

    )
