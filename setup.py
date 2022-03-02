#!/usr/bin/env python3

from setuptools import setup


setup(
    name="rfpkg-minimal",
    version="1.2.0",
    author="Dennis Gilmore",
    author_email="dgilmore@fedoraproject.org",
    description="Helper script for RPMFusion buildystem to fetch sources.",
    license="GPLv2+",
    url="https://github.com/rpmfusion-infra/rfpkg-minimal",
    scripts=["bin/rfpkg-minimal", "bin/rfpkg-base"],
    platforms="linux",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Operating System :: POSIX :: Linux",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Programming Language :: Unix Shell",
    ],
)
