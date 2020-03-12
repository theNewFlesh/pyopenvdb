# docker_pyopenvdb
OpenVDB for python 3.7
Creates a docker container, which is used to build and package pyopenvdb.

# Installation
### Currently only for linux systems with x86_64 archiutecture
1. pip install pyopenvdb
2. Find parent directory of pyopenvdb.so with `find / | grep -P 'pyopenvdb\.so`
3. `export LD_LIBRARY_PATH=`[parent directory]

# Installation
1. Install [docker](https://docs.docker.com/v17.09/engine/installation)
2. Install [docker-machine](https://docs.docker.com/machine/install-machine) (if running on macOS or Windows)
3. Ensure docker-machine has at least 4 GB of memory allocated to it.
4. `cd docker_pyopenvdb`
5. `chmod +x bin/pyopenvdb`
6. `bin/pyopenvdb start`

The service should take several minutes to start up.

Run `bin/pyopenvdb --help` for more help on the command line tool.

# Usage
`>>>python3.7`

`>>>import openvdb`
