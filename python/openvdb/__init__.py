import os

__msg = 'The pyopenvdb package currently only work on Linux x86_64 systems. '
__msg += 'Try running `find / | grep pyopenvdb.so` in a terminal. '
__msg += 'Find the parent directory of the pyopenvdb.so file and then run '
__msg += '`export LD_LIBRARY_PATH=[directory]` before running python.'

if 'LD_LIBRARY_PATH' not in os.environ:
    __msg = 'LD_LIBRARY_PATH environment variable not set. ' + __msg
    raise ImportError(__msg)
else:
    tmp = 'pyopenvdb.so not found in LD_LIBRARY_PATH environment variable. '
    __msg = tmp + __msg

    error = True
    ld_paths = os.environ['LD_LIBRARY_PATH'].split(':')
    for path in ld_paths:
        if os.path.exists(path) and 'pyopenvdb.so' in os.listdir(path):
            error = False
    if error:
        raise ImportError(__msg)

from pyopenvdb import *
