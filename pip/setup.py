from setuptools import setup
import os

DEPS = os.listdir('/tmp/docker_pyopenvdb/deps')
DEPS = {'': x for x in DEPS}

with open('version.txt') as f:
    VERSION = f.read().strip('\n')

with open('README.md') as f:
    README = f.read()
# ------------------------------------------------------------------------------

setup(
    name='pyopenvdb',
    packages=['deps'],
    version=VERSION,
    license='MPL version 2.0',
    description='Python bindings for Open Voxel Database',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Alex Braun',
    author_email='Alexander.G.Braun@gmail.com',
    url='https://github.com/theNewFlesh/docker_pyopenvdb',
    download_url='https://github.com/theNewFlesh/docker_pyopenvdb/archive/' + VERSION + '.tar.gz',
    keywords=['OpenVDB', 'pyopenvdb'],
    classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.7',
    ],
    package_data=DEPS,
)
