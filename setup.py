#!/usr/bin/env python
import os
import sys
from codecs import open

from setuptools import setup
from setuptools.command.test import test as TestCommand

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 10)
REQUIRED_PYTHON_STR = '.'.join([str(i) for i in REQUIRED_PYTHON])

if sys.version_info < REQUIRED_PYTHON:
    sys.exit(f"InstallError: Python {REQUIRED_PYTHON_STR} or newer is required.")

# 'setup.py publish' shortcut.
if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    sys.exit()

requires = [
    f"python_version >= '{REQUIRED_PYTHON_STR}'",
    # "charset_normalizer>=2,<4",
    # "idna>=2.5,<4",
    # "urllib3>=1.21.1,<3",
    # "certifi>=2017.4.17",
]
test_requirements = [
    # "pytest-httpbin==2.0.0",
    # "pytest-cov",
    # "pytest-mock",
    # "pytest-xdist",
    # "PySocks>=1.5.6, !=1.5.7",
    # "pytest>=3",
]

about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "src", "hell_rcon_core", "__version__.py"), "r", "utf-8") as f:
    exec(f.read(), about)

with open("README.md", "r", "utf-8") as f:
    readme = f.read()

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    packages=["hell_rcon_core"],
    package_data={"": ["LICENSE", "NOTICE"]},
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=f">={REQUIRED_PYTHON_STR}",
    install_requires=requires,
    license=about["__license__"],
)