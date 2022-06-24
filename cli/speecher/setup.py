from setuptools import setup, find_packages
import pathlib

setup(
    name="speecher",
    version="0.0.0",
    description="An cli for the Vosk api",
    url="https://github.com/cockernutx/speecher",
    packages=find_packages(where="speecher"),
    requires=["progress", "vosk"]
)