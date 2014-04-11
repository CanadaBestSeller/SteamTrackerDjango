from django.db import models
from django.utils.encoding import smart_unicode

from time import mktime
from datetime import datetime

import urllib
import re
import json
import time

# Create your models here.

class User(models.Model):
    firstName = models.CharField(max_length=120, null=True, blank=True)
    lastName = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.email)

class CsgoItem(models.Model):
    fullname = models.CharField(max_length=128, null=False, blank=False)
    url = models.CharField(max_length=256, null=False, blank=False)
    weapon = models.CharField(max_length=32)
    skin = models.CharField(max_length=32)
    exterior = models.CharField(max_length=32)
    statTrak = models.NullBooleanField()
    special = models.NullBooleanField()
    souvenir = models.NullBooleanField()
    star = models.NullBooleanField()
    volatility = models.DecimalField(max_digits=6, decimal_places=3, null=True)

    def __unicode__(self):
        return self.fullname

    def get_transactions(self):
        request = urllib.urlopen(self.url)
        source_code = request.read()

        pattern = "var line1=(\[\[.*?\]\]);"
        matches = re.search(pattern, source_code)
        transactions_string = matches.groups()[0]

        decoder = json.JSONDecoder()
        t_string_array = decoder.decode(transactions_string)
        t_array = map(Utils.transaction_string_array_to_transaction, t_string_array)

        return t_array

class CsgoItemTransaction(models.Model):
    csgo_item = models.ForeignKey('CsgoItem')
    time = models.DateTimeField(null=False, blank=False)
    average_price = models.FloatField()
    copies_sold = models.IntegerField(null=False, blank=False)

    def __unicode__(self):
        return self.csgo_item.fullname

class Utils:
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
