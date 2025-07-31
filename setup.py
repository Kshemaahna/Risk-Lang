# setup.py

from setuptools import setup, find_packages

setup(
    name='risklang',
    version='0.1',
    packages=find_packages(),
    install_requires=['lark'],
    entry_points={
        'console_scripts': [
            'risklang=cli:main',
        ],
    },
)

