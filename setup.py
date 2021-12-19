from setuptools import find_packages, setup

setup(
    name='large-file-finder',
    description='An awesome cli application to find large files in file system',
    version='1.0.0',
    author='Rahul Baruri',
    author_email='rahulbaruri1@gmail.com',
    url='http://pypi.python.org/pypi/large-file-finder/',
    license='LICENSE.txt',
    entry_points={
        'console_scripts': [
            'large-file-finder=app:initialize',
        ],
    },
    packages=find_packages(exclude=[".gitignore","screenshot.png","venv"]),
    package_dir={'app': ''},
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords=['large', 'file', 'finder', 'big file', 'filesize', 'monitor','detect huge file'],
    install_requires=[
        "halo",
        "tabulate",
    ],
    python_requires='>=3.4',
    project_urls={
    'Homepage': 'https://github.com/rbrahul/large-file-finder/',
    'Source': 'https://github.com/rbrahul/large-file-finder/',
    'Tracker': 'https://github.com/rbahul/large-file-finder/issues',
},
)
