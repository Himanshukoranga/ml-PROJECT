from setuptools import find_packages, setup
from typing import List

# Define the constant for the setup function later
HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function reads and returns the list of requirements
    from the specified file path.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        
    # Clean up whitespace and remove the newline character
    requirements = [req.replace("\n", "") for req in requirements]
    
    # Remove the '-e .' flag if it is present in the requirements list
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
        
    return requirements

# --- Main setup function ---
setup(
    name="my_package",
    version="0.1.0",
    # Corrected spelling of 'author'
    author="Himanshu",
    author_email="himanshukoranga1000@gmail.com",
    packages=find_packages(),
    
    # Calls the corrected function to get the dependencies
    install_requires=get_requirements('requirements.txt')
)  