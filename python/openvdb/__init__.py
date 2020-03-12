import os

__msg = 'The pyopenvdb package currently only work on Linux x86_64 systems. '
__msg += 'Try running `find / | grep pyopenvdb.so` in a terminal. '
__msg += 'Find the parent directory of the pyopenvdb.so file and then run '
__msg += '`export LD_LIBRARY_PATH=[directory]` before running python.'

if 'LD_LIBRARY_PATH' not in os.environ:
    __msg = 'LD_LIBRARY_PATH environment variable not set. ' + __msg
    raise ImportError(__msg)
elif 'pyopenvdb.so' not in os.listdir(os.environ['LD_LIBRARY_PATH']):
    __msg = 'pyopenvdb.so not found in LD_LIBRARY_PATH environment variable. ' + __msg
    raise ImportError(__msg)

from pyopenvdb import *
