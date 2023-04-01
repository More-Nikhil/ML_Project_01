from setuptools import find_packages,setup
from typing import List

Hypen_e_dot='-e .'
def get_requirements(file_path:str)->List[str]:
    '''This function will return the list of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements= [req.replace("\n","") for req in requirements]

        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)

    return requirements

setup(
    name="ML Project 01",
    version="0.0.1",
    author="Nikhil More",
    author_email="nmore7126@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements("requirements.txt")
)