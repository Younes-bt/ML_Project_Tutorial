from setuptools import find_packages, setup
from typing import List

to_remove = '-e .'
def get_requirement(file_path:str)->List[str]:
    requirement=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        [req.replace("\n", "") for req in requirement]
    
    if to_remove in requirement:
        requirement.remove(to_remove)
    
    return requirement


setup(
name='ML_Project_Tuto',
version='1.0',
author='Younes-BT',
author_email='bt.younesse@gmail.com',
packages=find_packages(),
install_requires=get_requirement('requirement.txt')

)
