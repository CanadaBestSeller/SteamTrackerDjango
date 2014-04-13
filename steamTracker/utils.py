from time import mktime, strftime
from datetime import datetime

import urllib
import re
import json
import time
import logging
import pprint

class Utils:
    @staticmethod
    def json_to_array(json_string):
        decoder = json.JSONDecoder()
        formatted_array = decoder.decode(json_string)
        return formatted_array

    @staticmethod
    def get_transactions_string_from_url(url):
        request = urllib.urlopen(url)
        source_code = request.read()

        pattern = "var line1=(\[\[.*?\]\]);"
        matches = re.search(pattern, source_code)
        transactions_string = matches.groups()[0]

        return transactions_string

    @staticmethod
    def datetime_string_to_datetime(date_string):
        pattern = "%a, %d %b %Y %H:%M:%S +0000"
        time_value = time.strptime(date_string, pattern)
        datetime_value = datetime.fromtimestamp(mktime(time_value))
        return datetime_value

    @staticmethod
    def sold_string_to_int(sold_string):
        return int(re.split(' ', sold_string)[0])

    @staticmethod
    def transaction_string_array_to_transaction(transaction_string_array):
        transaction_time = Utils.datetime_string_to_datetime(transaction_string_array[0])
        average_price = float(transaction_string_array[1])
        copies_sold = Utils.sold_string_to_int(transaction_string_array[2])
        return [transaction_time, average_price, copies_sold]

    @staticmethod
    def log(message):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        handler = logging.FileHandler('log.txt')
        handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter(Utils.now_as_string() + ' [%(levelname)s] %(name)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        logger.debug(pprint.pformat(message))

    @staticmethod
    def now_as_string():
        pattern = "%a, %b %d, %I:%M:%S %p"
        return strftime(pattern)
