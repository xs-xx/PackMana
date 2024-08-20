from setuptools import setup, find_packages

setup(
    name='PackMana',
    version='0.1',
    packages=find_packages(),
    install_requires=[
       "subprocess", "sys", "pkgutil", "ast", "inspecy","importlib"
        # You can list required packages here, if any
    ],
    author='Xses',
    author_email='xses.xs@gmail.com',
    description='A simple module to manage and install Python packages automatically.',
)
