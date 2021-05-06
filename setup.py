import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The test of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work for us
setup(
name = "cmc_csci46_vibingcat_datastructures",
version = "1.0,0"
description = "Data Strucutres Assignment",
long_description = "In README File",
long_description_content_type = "text/markdown",
url = "https://githubcom/nmpatterson22/Week-08/tree/master",
author = "Nohl Patterson",
author_email = "22mpatterson@gmail.com",
license = "MIT",
classifiers = [
"License :: OSI Approved :: MIT License",
"Programming Language :: Python :: 3",
"Programming Language :: Python :: 3.7",
],
packages = find_packages(exclude=("tests")),
include_packagedata = True,
install_requires = ["pytest", "hypothesis"],
)
