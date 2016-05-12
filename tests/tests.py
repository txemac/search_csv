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
        self.assertIsNotNone(db.products)

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

    def test_db_get_name_by_id(self):
        """
        Test DB. Get name by id
        """
        db = DB(filename=DATASET_TESTS_FILE)
        self.assertEqual('Miso Beaded Bracelets Pack Multi Multi', db.get_name_by_id(product_id=785))

    def test_db_get_name_by_id_invalid(self):
        """
        Test DB. Get name by id, with invalid id
        """
        db = DB(filename=DATASET_TESTS_FILE)
        self.assertRaises(ValueError, db.get_name_by_id, product_id=1)

    def test_db_get_brand_by_id(self):
        """
        Test DB. Get brand by id
        """
        db = DB(filename=DATASET_TESTS_FILE)
        self.assertEqual('Miso', db.get_brand_by_id(product_id=785))

    def test_db_get_brand_by_id_invalid(self):
        """
        Test DB. Get brand by id, with invalid id
        """
        db = DB(filename=DATASET_TESTS_FILE)
        self.assertRaises(ValueError, db.get_brand_by_id, product_id=1)

    def test_get_products_by_query(self):
        """
        Test DB. Get products by query
        """
        db = DB(filename=DATASET_TESTS_FILE)
        query = 'Multi'
        result = db.get_products_by_query(query=query)
        self.assertEqual(result, [('785', 50), ('8588', 30), ('12535', 15)], msg=result)

    def test_get_products_by_query2(self):
        """
        Test DB. Get products by query
        """
        db = DB(filename=DATASET_TESTS_FILE)
        query = 'See By'
        result = db.get_products_by_query(query=query)
        self.assertEqual(result, [('63602', 30)], msg=result)

    def test_get_products_by_query_none(self):
        """
        Test DB. Get products by query, with query = None
        """
        db = DB(filename=DATASET_TESTS_FILE)
        self.assertRaises(ValueError, db.get_products_by_query, query=None)

    def test_get_products_by_query_no_match(self):
        """
        Test DB. Get products by query, with query without matchs
        """
        db = DB(filename=DATASET_TESTS_FILE)
        query = 'aaaaaaa'
        result = db.get_products_by_query(query=query)
        self.assertEqual(result, [], msg=result)


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
