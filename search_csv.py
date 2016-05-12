import os
from db.db import DB
from settings import DATASET_FILE, QUERIES_FILE, DATASET_TESTS_FILE
from utils.read_files import read_queries_file

__author__ = 'josebermudez'


here = os.path.dirname(os.path.abspath(__file__))


if __name__ == '__main__':

    # Charge data base
    db = DB(filename=os.path.join(here, DATASET_FILE))

    # Get queries
    queries = read_queries_file(filename=os.path.join(here, QUERIES_FILE))
    # queries = ['Multi']

    for num, query in enumerate(queries):
        print num+1
        result = db.get_products_by_query(query)
        for key, value in result[:10]:
            print "%i,%i,%s,%s" % (int(value), int(key), db.get_name_by_id(product_id=key), db.get_brand_by_id(product_id=key))
