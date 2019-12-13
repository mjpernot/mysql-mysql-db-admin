#!/usr/bin/python
# Classification (U)

"""Program:  proc_all_dbs.py

    Description:  Unit testing of _proc_all_dbs in mysql_db_admin.py.

    Usage:
        test/unit/mysql_db_admin/proc_all_dbs.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import mock

# Local
sys.path.append(os.getcwd())
import mysql_db_admin
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


def func_holder(server, db, tbl, **kwargs):

    """Method:  func_holder

    Description:  Function stub holder for a generic function call.

    Arguments:
        server -> Server class instance.
        db -> Database name.
        tbl -> Table name.

    """

    pass


class Server(object):

    """Class:  Server

    Description:  Class stub holder for mysql_class.Server class.

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_all_dbs -> Test with processing all databases.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.func_name = func_holder
        self.db_list = ["db1", "db2"]
        self.db_list2 = []

    @mock.patch("mysql_db_admin.gen_libs.dict_2_list")
    @mock.patch("mysql_db_admin.mysql_libs.fetch_tbl_dict")
    def test_no_dbs(self, mock_fetch_tbl, mock_list):

        """Function:  test_no_dbs

        Description:  Test with processing no databases.

        Arguments:

        """

        mock_fetch_tbl.return_value = True
        mock_list.return_value = ["tbl1", "tbl2"]

        self.assertFalse(mysql_db_admin._proc_all_dbs(
            self.server, self.func_name, self.db_list2))

    @mock.patch("mysql_db_admin.gen_libs.dict_2_list")
    @mock.patch("mysql_db_admin.mysql_libs.fetch_tbl_dict")
    def test_all_dbs(self, mock_fetch_tbl, mock_list):

        """Function:  test_all_dbs

        Description:  Test with processing all databases.

        Arguments:

        """

        mock_fetch_tbl.return_value = True
        mock_list.return_value = ["tbl1", "tbl2"]

        self.assertFalse(mysql_db_admin._proc_all_dbs(
            self.server, self.func_name, self.db_list))


if __name__ == "__main__":
    unittest.main()
