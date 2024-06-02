from setuptools import setup,find_packages
from typing import List



#DECLAIRING VARIBLES FOR SETUP FUNCTIONS
PROJECT_NAME="housing_predictor" 
AUTHOR="Dev Ranjan Raut"
VERSION="0.0.2"
DESCRIPTION="This is my first ML end-to-end project"
PACKAGES=find_packages()
REQUIREMENT_FILE_NAME="requirements.txt"

'''
DESCRIPTION:FUNCTION WILL RETURN THE LIST OF LIBARRY MENTIONED IN requirements.txt FILE 
'''
def get_requirements_list()->List[str]:
    '''
    DESCRIPTION:FUNCTION WILL RETURN THE LIST OF LIBARRY MENTIONED IN requirements.txt FILE 
    '''
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
name=PROJECT_NAME ,
author=AUTHOR,
version=VERSION,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list(),
license="Apache License Version 2.0"
)

