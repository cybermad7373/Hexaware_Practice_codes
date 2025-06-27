from setuptools import setup, find_packages

setup(
    name="loan_management",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'mysql-connector-python',
        'pytest'
    ],
)