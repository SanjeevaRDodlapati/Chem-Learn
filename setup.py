from glob import glob
import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='chemlearn',
      version='0.0.0',
      description='Deep learning for chemistry',
      long_description=read('README.rst'),
      author='Sanjeeva Reddy Dodlapati',
      author_email='sdodl001@odu.edu',
      license="MIT",
      url='https://github.com/SanjeevaRDodlapati/Chem-Learn',
      packages=find_packages(),
      scripts=glob('./scripts/*.py'),
      install_requires=['h5py',
                        'argparse',
                        'pandas',
                        'numpy',
                        'pytest',
                        'torch',
                        'rdkit-pypi',
                        ],
      keywords=['Deep learning',
                'Deep neural networks',
                'Molecular graphs',
                'Drug discovery',
                'Drug target interaction'],
      classifiers=['Development Status :: 0 - developmet',
                   'Environment :: Console',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   'Programming Language :: Python :: 3.9',
                   'Topic :: Scientific/Engineering :: Artificial Intelligence',
                   'Topic :: Scientific/Engineering :: Chem-Informatics',
                   ]
      )
