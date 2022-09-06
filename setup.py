from setuptools import setup,find_packages
from typing import List

Project_Name = "housing predictor"
Version="0.0.1"
Author="jivitesh"
Description="This is housing prediction ML model"
Requirement_file_name="requirements.txt"


def get_requirements_list()->List[str]:
    with open(Requirement_file_name) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
name= Project_Name,
version=Version,
author=Author,
description=Description,
packages=find_packages(),
install_requires=get_requirements_list()
)

if __name__ == "__main__":
    print(get_requirements_list())