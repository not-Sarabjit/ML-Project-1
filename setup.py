from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)-> List[str]:
    '''
    This function will return a list with all the libraries in the given path
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=[r.replace('\n','') for r in file_obj.readlines() if '-e .' not in r]
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Sarabjit',
    author_email='sarabjit2807@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)