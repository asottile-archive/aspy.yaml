from setuptools import setup, find_packages


setup(
    name='aspy.yaml',
    description="A few extensions to pyyaml.",
    url='http://github.com/asottile/aspy.yaml',
    version='0.2.0',

    author='Anthony Sottile',
    author_email='asottile@umich.edu',

    platforms='all',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages(exclude=['tests*']),
    namespace_packages=['aspy'],
    install_requires=[
        'ordereddict',
        'pyyaml',
    ],
)
