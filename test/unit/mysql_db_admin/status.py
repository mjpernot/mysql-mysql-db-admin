#!/usr/bin/python
# Classification (U)

"""Program:  status.py

    Description:  Unit testing of status in mysql_db_admin.py.

    Usage:
        test/unit/mysql_db_admin/status.py

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


class Mail(object):

    """Class:  Mail

    Description:  Class stub holder for gen_class.Mail class.

    Methods:
        __init__ -> Class initialization.
        get_time -> Stub method holder for SlaveRep.get_time.
        get_name -> Stub method holder for SlaveRep.get_name.
        upd_slv_time -> Stub method holder for SlaveRep.upd_slv_time.

    """

    def __init__(self, lag_time=1):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        pass

    def add_2_msg(self, data):

        """Method:  add_2_msg

        Description:  Stub method holder for Mail.add_2_msg.

        Arguments:

        """

        return True

    def send_mail(self):

        """Method:  get_name

        Description:  Stub method holder for Mail.send_mail.

        Arguments:

        """

        return True


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

        self.name = "ServerName"
        self.cur_mem_mb = "cur_mem_mb"
        self.max_mem_mb = "max_mem_mb"
        self.prct_mem = "prct_mem"
        self.days_up = "days_up"
        self.cur_conn = "cur_conn"
        self.max_conn = "max_conn"
        self.prct_conn = "prct_conn"

    def upd_srv_stat(self):

        """Method:  upd_srv_stat

        Description:  Stub method holder for mysql_class.Server.upd_srv_stat.

        Arguments:

        """

        pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_mail -> Test with emailing out.
        test_file -> Test with writing to file.
        test_mongo -> Test with mongo connection.
        test_non_json -> Test with in non-JSON format.
        test_json -> Test with in JSON format.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()
        self.mail = Mail()
        self.args_array = {"-j": True, "-z": True}
        self.args_array2 = {}

    @mock.patch("mysql_db_admin.mongo_libs.ins_doc")
    @mock.patch("mysql_db_admin.gen_libs.write_file")
    def test_mail(self, mock_write, mock_mongo):

        """Function:  test_mail

        Description:  Test with emailing out.

        Arguments:

        """

        mock_write.return_value = True
        mock_mongo.return_value = True

        self.assertFalse(mysql_db_admin.status(self.server, self.args_array,
                                               mail=self.mail))

    @mock.patch("mysql_db_admin.mongo_libs.ins_doc")
    @mock.patch("mysql_db_admin.gen_libs.write_file")
    def test_file(self, mock_write, mock_mongo):

        """Function:  test_file

        Description:  Test with writing to file.

        Arguments:

        """

        mock_write.return_value = True
        mock_mongo.return_value = True

        self.assertFalse(mysql_db_admin.status(self.server, self.args_array,
                                               ofile="FileName"))

    @mock.patch("mysql_db_admin.mongo_libs.ins_doc")
    @mock.patch("mysql_db_admin.gen_libs.write_file")
    def test_mongo(self, mock_write, mock_mongo):

        """Function:  test_mongo

        Description:  Test with mongo connection.

        Arguments:

        """

        mock_write.return_value = True
        mock_mongo.return_value = True

        self.assertFalse(mysql_db_admin.status(self.server, self.args_array,
                                               class_cfg="Cfg",
                                               db_tbl="db:tbl"))

    def test_non_json(self):

        """Function:  test_non_json

        Description:  Test with in non-JSON format.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(mysql_db_admin.status(self.server,
                                                   self.args_array2))

    @mock.patch("mysql_db_admin.mongo_libs.ins_doc")
    @mock.patch("mysql_db_admin.gen_libs.write_file")
    def test_json(self, mock_write, mock_mongo):

        """Function:  test_json

        Description:  Test with in JSON format.

        Arguments:

        """

        mock_write.return_value = True
        mock_mongo.return_value = True

        self.assertFalse(mysql_db_admin.status(self.server, self.args_array))


if __name__ == "__main__":
    unittest.main()
