#!/usr/bin/env python

import os.path
from distutils.core import setup

README = open(os.path.join(os.path.dirname(__file__), "README.rst")).read()

CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Web Environment",
    "Framework :: Django",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: System :: Networking",
]


import pushapp

setup(
    name="django-pushapp",
    packages=[
        "pushapp",
        "pushapp/migrations",
        "pushapp/management",
        "pushapp/management/commands",
    ],
    author=pushapp.__author__,
    author_email=pushapp.__email__,
    classifiers=CLASSIFIERS,
    description="Send push notifications to mobile devices through GCM or APNS in Django.",
    download_url="https://github.com/pirsipy/django-pushapp/tarball/master",
    long_description=README,
    url="https://github.com/pirsipy/django-pushapp",
    version=pushapp.__version__,
)
