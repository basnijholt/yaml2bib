#!/usr/bin/env python

import sys

from setuptools import find_packages, setup

if sys.version_info < (3, 6):
    print("yaml2bib requires Python 3.6 or above.")
    sys.exit(1)

with open("README.md") as f:
    readme = f.read()

extras_require = dict(
    docs=[
        "sphinx",
        "sphinx-rtd-theme",
        "m2r",  # markdown support
        "sphinxcontrib.apidoc",  # run sphinx-apidoc when building docs
    ],
    dev=["pre-commit", "bump2version"],
    test=["pytest", "pytest-cov", "tox"],
)

install_requires = [
    "Click",
    "crossrefapi",
    "diskcache",
    "requests",
    "pylatexenc",
    "pyyaml",
    "tqdm",
]


setup(
    name="yaml2bib",
    python_requires=">=3.6",
    version="0.1.3",
    classifiers=[
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Convert a yaml file containing (key -> DOI) pairs to bib file with the correct journal abbreviations.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/basnijholt/yaml2bib",
    author="Bas Nijholt",
    author_email="basnijholt@gmail.com",
    license="MIT",
    packages=find_packages("."),
    entry_points={"console_scripts": ["yaml2bib=yaml2bib:_yaml2bib.cli"]},
    install_requires=install_requires,
    extras_require=extras_require,
    zip_safe=False,
)
