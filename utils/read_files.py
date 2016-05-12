# coding=utf-8
import csv

import codecs
import os

__author__ = 'josebermudez'


def read_csv_file(filename):
    """
    Read csv file and get the model
    :param filename: filename
    :return: model
    """
    if not filename:
        raise ValueError('Empty filename value.')
    if not os.path.isfile(filename):
        raise IOError('File does not exist.')

    f_in = open(filename, 'rU')
    reader = csv.reader(codecs.open(filename, 'rU'))

    # model
    model = dict()

    # loop for rows in reader
    for product_id, name, brand in reader:
        model[product_id] = dict(
            name=name,
            brand=brand
        )

    # Close file
    f_in.close()

    return model


# TODO: problem with repeat IDs

# TODO: ascii chars


def read_queries_file(filename):
    """
    Read a query file
    :param filename: filename
    :return: list of querys
    """
    if not filename:
        raise ValueError('Empty filename value.')
    if not os.path.isfile(filename):
        raise IOError('File does not exist.')

    f_in = open(filename, 'r')

    queries = []

    for row in f_in.readlines():
        queries.append(row[:-1])

    f_in.close()

    return queries
