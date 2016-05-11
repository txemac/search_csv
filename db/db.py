from utils.csvfiles import read_csv_file


__author__ = 'josebermudez'


class DB(object):

    def __init__(self, filename):
        if not filename:
            raise ValueError('You need a file. Check settings file.')

        self.filename = filename
        self.model = {}
        self.model = read_csv_file(filename=self.filename)

