from setuptools import setup, find_packages

with open("requirements.txt", 'r') as file:
    requirements = file.readlines()

setup(
    name='PyCrowlingo',
    version='0.1',
    packages=find_packages(),
    install_requires=requirements,
    extras_require={
        'rasa': ["rasa"]
    },
    license='copyright: Crowlingo',
    author='Jonas Bouaziz',
    description='Crowlingo SDK for easy communication with APIs.'
)
