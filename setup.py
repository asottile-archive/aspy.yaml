from setuptools import find_packages
from setuptools import setup


setup(
    name='aspy.yaml',
    description="A few extensions to pyyaml.",
    url='https://github.com/asottile/aspy.yaml',
    version='1.1.2',

    author='Anthony Sottile',
    author_email='asottile@umich.edu',

    platforms='all',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages(exclude=('tests*', 'testing*')),
    install_requires=['pyyaml'],
)
