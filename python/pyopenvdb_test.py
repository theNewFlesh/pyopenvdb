from pathlib import Path
import unittest

import pytest
# ------------------------------------------------------------------------------


class PyOpenVDBTests(unittest.TestCase):
    def test_import(self):
        import pyopenvdb

    def test_numpy(self):
        import pyopenvdb as vdb
        cube = Path(Path(__file__).parent.parent, 'resources', 'cube.vdb')\
            .absolute()\
            .as_posix()
        result = vdb.readAll(cube)[0][0].convertToPolygons(0.1)
        self.assertEqual(len(result), 3)
