from setuptools import setup


setup(
    name='aspy.yaml',
    description="A few extensions to pyyaml.",
    url='http://github.com/asottile/aspy.yaml',
    version='0.2.1',

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

    packages=['aspy', 'aspy.yaml'],
    namespace_packages=['aspy'],
    install_requires=[
        'ordereddict',
        'pyyaml',
    ],
)
