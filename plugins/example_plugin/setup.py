# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    LONG_DESC = fh.read()
    setup(
        name="hydra-example",
        version="0.1.0",
        author="Omry Yadan",
        author_email="omry@fb.com",
        description="Example plugin for hydra",
        long_description=LONG_DESC,
        long_description_content_type="text/markdown",
        url="https://github.com/facebookresearch/hydra/",
        packages=find_packages(exclude=["tests"]),
        classifiers=[
            # Python versions are used by the noxfile in Hydra to determine which
            # python versions to test this plugin with
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Operating System :: OS Independent",
        ],
        install_requires=[],
    )
