from utils.read_files import read_csv_file


__author__ = 'josebermudez'


class DB(object):

    def __init__(self, filename):
        self.filename = filename
        self.model = {}
        self.model = read_csv_file(filename=self.filename)
