from setuptools import setup, find_packages

with open("requirements.txt", 'r') as file:
    requirements = file.readlines()

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='PyCrowlingo',
    version='0.6.2',
    packages=find_packages(),
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type='text/markdown',
    extras_require={
        'rasa': ["rasa"]
    },
    url='https://github.com/Crowlingo/PyCrowlingo/',
    license='copyright: Crowlingo',
    author='Jonas Bouaziz',
    description='Official Crowlingo SDK. Access to all NLP and NLU services that analyze texts regardless of the '
                'language. '
)
