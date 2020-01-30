# docker_pyopenvdb
OpenVDB for python 3.7

# Usage
`>>>python3.7`
`>>>import pyopenvdb`

# Additional Install
  * Just copy /usr/lib/python3.7/pyopenvdb.so into whatever directory your
    python3.7 interpreter looks at.
  * LD_LIBRARY_PATH is an environment variable that links pyopenvdb.so to its
    C/C++ dependencies. It is set via the dockerfile, but call
    `env | grep LD_LIBRARY_PATH` to ensure that it is set in your environment.
