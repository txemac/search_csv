import operator

from collections import Counter
from settings import POINTS_TOKEN, POINTS_PREFIX, POINTS_MUL_NAME, POINTS_MUL_BRAND
from utils.read_files import read_csv_file


__author__ = 'josebermudez'


class DB(object):

    def __init__(self, filename):
        self.filename = filename
        self.products = read_csv_file(filename=self.filename)
        self.index_names, self.index_brands = self.__index_words()

    def __index_words(self):
        """
        Get the index dictionaries for names and brands
        :return: names and brands
        """
        names = dict()
        brands = dict()

        for key, value in self.products.iteritems():
            for name in value['name'].split():
                names.setdefault(name, []).append(key)
            for brand in value['brand'].split():
                brands.setdefault(brand, []).append(key)

        return names, brands

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

    def get_products_by_query(self, query):
        """
        Get matchs with score by query
        :param query:
        :return:
        """
        scores = []

        words = query.split()
        for word in words:
            scores.append(self.__get_score(word=word))

        # sum dictionaries
        for item in scores[1:]:
            scores[0] = dict(Counter(scores[0]) + Counter(item))

        # sort by score
        query_score = sorted(scores[0].items(), key=operator.itemgetter(0))

        return query_score

    def __get_score(self, word):
        """
        Get score for a word
        :param word: word
        :return: score
        """
        score = dict()
        names = []
        brands = []

        # tokens
        if word in self.index_names.keys():
            names = self.index_names[word]
        if word in self.index_brands.keys():
            brands = self.index_brands[word]
        tokens = names * POINTS_MUL_NAME + brands * POINTS_MUL_BRAND

        # prefixes
        names = self.__get_prefixes(self.index_names, word)
        brands = self.__get_prefixes(self.index_brands, word)
        prefixes = names * POINTS_MUL_NAME + brands * POINTS_MUL_BRAND

        for product_id in tokens:
            if product_id in score.keys():
                score[product_id] += POINTS_TOKEN
            else:
                score[product_id] = POINTS_TOKEN

        for product_id in prefixes:
            if product_id in score.keys():
                score[product_id] += POINTS_PREFIX
            else:
                score[product_id] = POINTS_PREFIX

        return score

    def __get_prefixes(self, dictionary, word):
        """
        Get list of ids with prefixes in dictionary
        :param dictionary: dictionary
        :param word: word
        :return: list of ids
        """
        result = []
        for key, value in dictionary.iteritems():
            if key.startswith(word):
                result = result + list(set(value) - set(result))
        return result
