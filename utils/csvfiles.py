import csv
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
    reader = csv.reader(f_in, dialect=csv.excel_tab)

    # model
    model = {}

    # loop for rows in reader
    for row in reader:
        id, name, brand = row[0].split(',')
        model[id] = {
            'name': name,
            'brand': brand
        }

    # Close file
    f_in.close()

    return model
