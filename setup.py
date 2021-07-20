#!/usr/bin/env python

"""The setup script."""

import os
from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

# with open("HISTORY.rst") as history_file:
#     history = history_file.read()

requirements = [
    "numpy>=1.20.2",
    "torch==1.8.0",
    "astropy>=4.2.1",
    "scikit-image>=0.18.1",
    "scikit-learn>=0.24.2",
    "sep>=1.1.1",
    "tensorboard>=2.4.1",
    "reproject>=0.7.1",
    "Flask>=1.1.2",
    "Flask-APScheduler>=1.12.2",
    "psutil>=5.8.0",
    "pretty-errors",
    "tqdm",
]

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest>=3",
    "pip",
    "bump2version",
    "wheel",
    "watchdog",
    "flake8",
    "tox",
    "coverage",
    "Sphinx",
    "twine",
]

setup(
    author="Chengyuan Xu, Curtis McCully, Boning Dong, D. Andrew Howell, and Pradeep Sen",
    author_email="cxu@ucsb.edu",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.7",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Environment :: GPU :: NVIDIA CUDA",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Scientific/Engineering :: Astronomy",
    ],
    description="Cosmic-CoNN: A Cosmic Ray Detection Deep Learning Framework, Dataset, and Toolkit",
    entry_points={
        "console_scripts": [
            "cosmic-conn=cosmic_conn.inference_cr:CLI_entry_point",
            "cosmic_conn=cosmic_conn.inference_cr:CLI_entry_point",
        ],
    },
    install_requires=requirements,
    dependency_links=[
        '-f https://download.pytorch.org/whl/torch_stable.html'],
    license="GNU General Public License v3",
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords="cosmic_conn",
    name="cosmic_conn",
    packages=find_packages(include=[
        "cosmic_conn",
        "cosmic_conn.*",
        "cr_pipeline",
        "dl_framework",
        "evaluate",
        "web_app",
    ]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/cy-xu/cosmic-conn",
    version="0.2.3",
    zip_safe=False,
)
