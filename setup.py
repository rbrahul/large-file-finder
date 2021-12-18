from setuptools import setup

setup(
    name='bigfile',
    version='0.1.0',
    author='Rahul Baruri',
    author_email='rahulbaruri1@gmail.com',
    packages=['big_file_finder'],
    scripts=['bin/script1', 'bin/script2'],
    url='http://pypi.python.org/pypi/PackageName/',
    license='LICENSE.txt',
    description='An awesome package that does something',
    long_description=open('README.txt').read(),
    install_requires=[
        "Django >= 1.1.1",
         "pytest",
    ],
)
