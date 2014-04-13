from steamTracker.models import CsgoItem, Utils
import urllib
i = CsgoItem()
i.fullname = "Example Item"
i.url = "http://steamcommunity.com/market/listings/730/Tec-9%20%7C%20Army%20Mesh%20%28Field-Tested%29"
i.save()

from steamTracker.models import CsgoItem
t = CsgoItem.objects.get().get_transactions()
Utils.transaction_string_array_to_transaction(t[0])

# Logging
# create logger with 'spam_application'
import logging
logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

logger.debug('TEST')