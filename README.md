# docker_pyopenvdb
OpenVDB for python 3.7
Creates a docker container, which is used to build and package pyopenvdb.

# Installation
1. pip install numpy
2. pip install pyopenvdb
3. `export LD_LIBRARY_PATH=`[parent directory of pyopenvdb.so]

# Installation
1. Install [docker](https://docs.docker.com/v17.09/engine/installation)
2. Install [docker-machine](https://docs.docker.com/machine/install-machine) (if running on macOS or Windows)
3. Ensure docker-machine has at least 4 GB of memory allocated to it.
4. `cd docker_pyopenvdb`
5. `chmod +x bin/docker_pyopenvdb`
6. `bin/docker_pyopenvdb start`

The service should take several minutes to start up.

Run `bin/docker_pyopenvdb --help` for more help on the command line tool.

# Usage
`>>>python3.7`

`>>>import pyopenvdb`
