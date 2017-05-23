class Ticket(object):
    """ This class represents a ticket for an event """

    def __init__(self, price):
        self._price = price

    # Implement this ourselves to keep ticket list of an event sorted when new tickets are inserted
    def __lt__(self, cmp):
        return self._price < cmp.price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price
