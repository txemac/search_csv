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
    model = {}

    # loop for rows in reader
    for row in reader:
        model[row[0]] = {
            'name': row[1],
            'brand': row[2]
        }

    # Close file
    f_in.close()

    return model


# TODO: problem with repeat IDs


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
