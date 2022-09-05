from setuptools import setup
from typing import List

Project_Name = "housing predictor"
Version="0.0.1"
Author="jivitesh"
Description="This is housing prediction ML model"
Packages=["housing"]
Requirement_file_name="requirements.txt"


def get_requirements_list()->List[str]:
    with open(Requirement_file_name) as requirement_file:
        requirement_file.readlines()


setup(
name= Project_Name,
version=Version,
author=Author,
description=Description,
packages=Packages,
install_requires=get_requirements_list()
)

if __name__ == "__main__":
    print(get_requirements_list())