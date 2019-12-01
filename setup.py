"""Packaging settings."""
from setuptools import find_packages, setup

from src.f_cli import __version__


INSTALL_REQUIRES = [
    'click~=7.0'
]

TEST_REQUIRES = [
    'flake8~=3.5',
    'flake8-docstrings~=1.3',
    'mypy~=0.610',
    'pep8-naming~=0.7',
    'pydocstyle<4.0.0',
    'pylint~=2.0',
    'pytest~=5.1'
]

setup(
    name='f-cli',
    version=__version__,
    description='Cloud Engineer toolkit',
    long_description='Cloud Engineer toolkit',
    url='https://github.com/ITProKyle/f-cli',
    author='Kyle Finley',
    author_email='kyle@finley.sh',
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Utilities'
    ],
    python_requires='>=3.7',
    keywords=['aws', 'cli'],
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    install_requires=INSTALL_REQUIRES,
    tests_require=TEST_REQUIRES,
    extras_require={
        'testing': TEST_REQUIRES
    },
    entry_points={
        'console_scripts': [
            'f-cli=f_cli.cli:main'
        ]
    },
    test_suite='tests',
    options={
        'bdist_wheel': {
            'python_tag': 'py3'
        }
    }
)
