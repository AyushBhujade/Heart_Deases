from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    requirements_list:List[str]=[]
    
    try:
        with open('requirements.txt','r')as file:
            lines=file.readlines()
            
            for line in lines:
                # strip whitespaces and newline charector
                requirements=line.strip()
                
                if requirements and requirements != '-e .':
                    requirements_list.append(requirements)
    except FileNotFoundError:
        print("requirements.tst file not found")
    
    return requirements_list
setup(
    name="HeartDiseses",
    version='0.0.1',
    author="Ayush Bhujade",
    author_email="ayushbhujade2005@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)