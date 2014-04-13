from django.db import models
from django.utils.encoding import smart_unicode

from steamTracker.utils import Utils

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
        transactions_string = Utils.get_transactions_string_from_url(self.url)
        t_string_array = Utils.json_to_array(transactions_string)
        t_array = map(Utils.transaction_string_array_to_transaction, t_string_array)
        return t_array

class CsgoItemTransaction(models.Model):
    csgo_item = models.ForeignKey('CsgoItem')
    time = models.DateTimeField(null=False, blank=False)
    average_price = models.FloatField()
    copies_sold = models.IntegerField(null=False, blank=False)

    def __unicode__(self):
        return self.csgo_item.fullname
