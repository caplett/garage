"""setuptools based setup module."""
import os
import sys

from setuptools import find_packages, setup

GARAGE_GH_TOKEN = os.environ.get('GARAGE_GH_TOKEN') or 'git'
GYM_VERSION = '0.17.2'

# Required dependencies
REQUIRED = [
    # Please keep alphabetized
    'akro>=0.0.8',
    'click>=2.0',
    'cloudpickle',
    'cma==2.7.0',
    'dowel>=0.0.3',
    'numpy>=1.14.5',
    'psutil',
    'python-dateutil',
    'ray',
    'scikit-image',
    'scipy',
    'sklearn',
    'setproctitle>=1.0',
    'torch>=1.0.0,!=1.5.0,<1.8.0',
    'torchvision>=0.2.1,<=0.8.2',
]

if sys.version_info < (3, 7):
    REQUIRED.append('dataclasses==0.7')

# Dependencies for optional features
EXTRAS = {}

# Make tensorflow optional
EXTRAS['tensorflow'] = [
    'tensorflow>=2.4,!=2.5.0',
    # This tensorflow version corresponds to the version required by
    # tensorflow-probability 0.12.
    # They don't declare their tensorflow version requirements, so that
    # users can choose to install tensorflow or tensorflow-gpu.
    'tensorflow-probability>=0.11.0,<=0.12.2',
]

EXTRAS['gym'] = [
    f'gym[atari,box2d,classic_control]=={GYM_VERSION}',
    'atari-py<0.2.7',
]

EXTRAS['mujoco'] = [
    'mujoco-py>=2.0,<=2.0.2.8',
    # Currently gym is not compatible with mujoco 2.0 because of poor
    # performance. So here we just install imageio to meet the dependency
    # requirement of gym's mujoco extra.
    'imageio',
]

EXTRAS['dm_control'] = [
    # dm_control throws an error during install about not being able to
    # find a build dependency (absl-py). Later pip executes the `install`
    # command again and the install succeeds because absl-py has been
    # installed. This is stupid, but harmless.
    'dm_control',
]

EXTRAS['bullet'] = ['mpi4py', 'pybullet>=2.8.7']

EXTRAS['all'] = list(set(sum(EXTRAS.values(), [])))

EXTRAS['tensorflow1'] = [
    # This version is not tested regularly, but should work.
    'tensorflow>=1.14,<2',
    'tensorflow-probability<0.9',
]

# Development dependencies (*not* included in 'all')
EXTRAS['dev'] = [
    # Please keep alphabetized
    'flake8',
    'flake8-docstrings>=1.5.0',
    'flake8-import-order',
    f'metaworld @ https://{GARAGE_GH_TOKEN}@api.github.com/repos/rlworkgroup/metaworld/tarball/0875192baaa91c43523708f55866d98eaf3facaf',  # noqa: E501
    'isort>=4.3.21,<5.0.0',
    'pep8-naming==0.7.0',
    'pre-commit',
    'pycodestyle>=2.5.0',
    'pydocstyle>=4.0.0',
    'pylint>=2.5.3',
    'pytest>=4.5.0',  # Required for strict-markers
    'pytest-cov',
    'pytest-rerunfailures',
    'pytest-timeout',
    'pytest-xdist',
    'recommonmark',
    'sphinx',
    'sphinx-autoapi>=1.4.0',
    'sphinx_rtd_theme',
    'sphinxcontrib-bibtex',
    'yapf==0.30.0',
]  # yapf: disable

with open('README.md', encoding='UTF-8') as f:
    README = f.read()

# Get the package version dynamically
with open('VERSION', encoding='UTF-8') as v:
    VERSION = v.read().strip()

setup(
    name='garage',
    version=VERSION,
    author='Reinforcement Learning Working Group',
    description='A toolkit for reproducible reinforcement learning research',
    url='https://github.com/rlworkgroup/garage',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    scripts=['scripts/garage'],
    python_requires='>=3.6',
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='MIT',
    long_description=README,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries',
    ],
)
