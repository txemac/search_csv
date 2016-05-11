import unittest

from db.db import DB
from settings import DATASET_TESTS_FILE, QUERIES_FILE
from utils.read_files import read_csv_file, read_queries_file


__author__ = 'josebermudez'


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

    def test_csv_files_read_file(self):
        """
        Test CSV Files. Read CSV file
        """
        model = read_csv_file(filename=DATASET_TESTS_FILE)
        self.assertIsNotNone(model)

    def test_csv_files_read_file_filename_none(self):
        """
        Test CSV Files. Read CSV file, with filename = None
        """
        self.assertRaises(ValueError, read_csv_file, filename=None)

    def test_csv_files_read_file_filename_invalid(self):
        """
        Test CSV Files. Read CSV file, with invalid filename
        """
        self.assertRaises(IOError, read_csv_file, filename='error.csv')


class TestQueriesFiles(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestQueriesFiles, self).__init__(*args, **kwargs)

    def test_queries_files_read_file(self):
        """
        Test Queries Files. Read Queries file
        """
        queries = read_queries_file(filename=QUERIES_FILE)
        self.assertIsNotNone(queries)
        self.assertEqual(queries[0], 'yellow toywatch')

    def test_queries_files_read_file_filename_none(self):
        """
        Test Queries Files. Read Queries file, with filename = None
        """
        self.assertRaises(ValueError, read_queries_file, filename=None)

    def test_queries_files_read_file_filename_invalid(self):
        """
        Test Queries Files. Read CSV file, with invalid filename
        """
        self.assertRaises(IOError, read_queries_file, filename='error.txt')
