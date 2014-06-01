from setuptools import setup


setup(
    name='asottile.yaml',
    description="asottile's extensions to pyyaml.",
    url='http://github.com/asottile/asottile.yaml',
    version='0.1.0',

    author='Anthony Sottile',
    author_email='asottile@umich.edu',

    platforms='all',
    classifiers=[
        'License :: Public Domain',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=['asottile.yaml'],
    namespace_packages=['asottile'],
    install_requires=[
        'asottile.ordereddict',
        'pyyaml',
    ],
)
