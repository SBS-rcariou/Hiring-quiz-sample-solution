# Used to install the package using PIP

import setuptools

setuptools.setup(
    name="quiz",
    version="0.1",
    author="Raphael",
    description="Inspect a large collection of positive integers",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)