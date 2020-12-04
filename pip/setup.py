from setuptools import setup

with open('version.txt') as f:
    VERSION = f.read().strip('\n')

with open('prod_requirements.txt') as f:
    PROD_REQUIREMENTS = f.read().split('\n')

with open('README.md') as f:
    README = f.read()
# ------------------------------------------------------------------------------

setup(
    name='pyopenvdb-3.8',
    version=VERSION,
    license='MPL version 2.0',
    description='Python bindings for Open Voxel Database for python 3.8',
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
      'Programming Language :: Python :: 3.8',
    ],
    packages=['openvdb'],
    install_requires=PROD_REQUIREMENTS,
)
