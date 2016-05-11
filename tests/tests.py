import unittest

import os
from db.db import DB
from settings import DATASET_TESTS_FILE
from utils.csvfiles import read_csv_file

__author__ = 'josebermudez'


here = os.path.dirname(os.path.abspath(__file__))


class TestDB(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestDB, self).__init__(*args, **kwargs)

    def test_db_create(self):
        """
        Test DB. Create DB
        """
        db = DB(filename=DATASET_TESTS_FILE)
        self.assertIsNotNone(db.model)

    def test_db_create_filename_none(self):
        """
        Test DB. Create DB, with filename = None
        """
        self.assertRaises(ValueError, DB, filename=None)

    def test_db_create_filename_invalid(self):
        """
        Test DB. Create DB, with invalid filename
        """
        self.assertRaises(IOError, DB, filename='error.csv')


class TestCSVFiles(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestCSVFiles, self).__init__(*args, **kwargs)

    def test_csvfiles_read_file(self):
        """
        Test CSV File. Read CSV file
        """
        model = read_csv_file(filename=DATASET_TESTS_FILE)
        self.assertIsNotNone(model)

    def test_csvfiles_read_file_filename_none(self):
        """
        Test CSV File. Read CSV file, with filename = None
        """
        self.assertRaises(ValueError, read_csv_file, filename=None)

    def test_csvfiles_read_file_filename_invalid(self):
        """
        Test CSV File. Read CSV file, with invalid filename
        """
        self.assertRaises(IOError, read_csv_file, filename='zz.csv')
