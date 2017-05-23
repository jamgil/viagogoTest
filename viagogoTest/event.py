import bisect

from .ticket import Ticket


class Event(object):
    """ Event class represents and manipulates real world events """

    # Auto-increment the event id when objects are created
    uid = 1

    def __init__(self, coordinate, tickets=None):
        if tickets is None:
            tickets = []
        self._uid = Event.uid
        Event.uid += 1
        self._tickets = tickets
        self._coordinate = coordinate

    # Custom printable representation for when we're listing events
    def __repr__(self):
        return f"Event#{self._uid}"

    @property
    def id(self):
        return self._uid

    @property
    def coordinate(self):
        return self._coordinate

    @coordinate.setter
    def coordinate(self, coordinate):
        self._coordinate = coordinate

    @property
    def tickets(self):
        return self._tickets

    def add_ticket(self, ticket):
        """ Using property based setters for a list field can cause confusion here.
            `event_obj.tickets = new_ticket` would append to the ticket list, rather than overriding the existing value.
            I've opted to use a regular method instead, for more clarity.
        """
        if isinstance(ticket, Ticket):
            # Keep list sorted by price when appended
            bisect.insort_left(self._tickets, ticket)
        else:
            raise TypeError("This method accepts a single Ticket object as an argument")

    def remove_ticket(self, ticket):
        if ticket in self._tickets:
            self._tickets.remove(ticket)

    def get_cheapest_ticket(self):
        return self.tickets[0] if self.tickets else None

    def get_distance_from_coord(self, coord):
        """ Implementation of Manhattan distance """
        return abs(self.coordinate.x - coord.x) + abs(self.coordinate.y - coord.y)

