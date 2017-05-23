import random

from .constants import X_LIMIT, Y_LIMIT
from .coordinate import Coordinate
from .event import Event
from .ticket import Ticket


class Grid(object):
    """ This class represents a grid which contains events at specific coordinates """
    def __init__(self):
        self._x_limit = X_LIMIT
        self._y_limit = Y_LIMIT
        self._coordinates = {}

    @property
    def x_limit(self):
        return self._x_limit

    @property
    def y_limit(self):
        return self._y_limit

    @property
    def coordinates(self):
        return self._coordinates

    def create_event(self, coord):
        event = Event(coord)
        self.coordinates[coord] = event
        return event

    def get_nearest_events(self, coord, num_events):
        coords = self.coordinates.copy()
        nearest_events = []
        for key, value in coords.items():
            if value.tickets and len(value.tickets) > 0:
                nearest_events.append([value, value.get_distance_from_coord(coord)])

        # Store calculated distance while iterating over event list so it can be easily sorted
        nearest_events.sort(key=lambda i: i[1], reverse=False)
        return nearest_events[:num_events]

    def populate_grid_random_data(self):
        for i in range(50):
            coord = self.get_random_coord()
            event = self.create_event(coord)
            self.generate_random_tickets_for_event(event)

    def get_random_coord(self):
        x = random.randint(self.x_limit[0], self.x_limit[1])
        y = random.randint(self.y_limit[0], self.y_limit[1])
        coord = Coordinate(x, y)
        return coord

    def generate_random_tickets_for_event(self, event):
        for i in range(0, random.randint(1, 10)):
            ticket = Ticket(round(random.uniform(15, 50), 2))
            event.add_ticket(ticket)
