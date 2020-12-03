import setuptools
from distutils.core import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='demo2',
    version='1.0',
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    description='Demo 2',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Heiko Schmidle',
    url='https://github.com/heikoschmidle/demo',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
    ]
)
