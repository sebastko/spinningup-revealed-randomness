from os.path import join, dirname, realpath
from setuptools import setup, find_packages
import sys

assert sys.version_info.major == 3 and sys.version_info.minor >= 6, \
    "The Spinning Up repo is designed to work with Python 3.6 and greater." \
    + "Please install it before proceeding."

with open(join("spinup", "version.py")) as version_file:
    exec(version_file.read())

setup(
    name='spinup',
    packages=find_packages(include=['spinup']),
    version='0.2',

    # Minimal set of requirements to use spinningup as a library.
    # Caution: not all functionality will work with just these dependencies. See the original spinningup repo
    # for the full list, or install with 'pip install .[extras]'.
    install_requires=[
        'gym',
        'joblib',
        'mpi4py',
        'numpy',
        'scipy',
        'torch',
        'tqdm',
        'psutil',
        # Unfortunately it would require too many changes to drop this dependency.
        'tensorflow>=1.8.0,<2.0'
    ],
    extras_require={
        'extras': ['cloudpickle==1.2.1', 'matplotlib==3.1.1', 'pandas', 'pytest', 'seaborn==0.8.1']
    },
    description="Teaching tools for introducing people to deep RL.",
    author="Joshua Achiam",
)
