from utils.read_files import read_csv_file


__author__ = 'josebermudez'


class DB(object):

    def __init__(self, filename):
        self.filename = filename
        self.products = read_csv_file(filename=self.filename)

    def __get_product_by_id(self, product_id):
        """
        Get product by id
        :param product_id: id
        :return: product
        """
        if str(product_id) not in self.products.keys():
            raise ValueError('The id does not exist.')
        return dict(
            id=str(product_id),
            data=self.products[str(product_id)]
        )

    def get_name_by_id(self, product_id):
        """
        Get name from id
        :param product_id: id
        :return: name
        """
        return self.__get_product_by_id(product_id=product_id)['data']['name']

    def get_brand_by_id(self, product_id):
        """
        Get brand from id
        :param product_id: id
        :return: brand
        """
        return self.__get_product_by_id(product_id=product_id)['data']['brand']
