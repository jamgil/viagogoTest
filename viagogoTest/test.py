import unittest

from .ticket import Ticket
from .coordinate import Coordinate
from .grid import Grid


class Test(unittest.TestCase):
    def test(self):
        # Test distance calculation
        grid = Grid()
        event = grid.create_event(Coordinate(1, 1))
        self.assertEqual(event.get_distance_from_coord(Coordinate(2, 2)), 2)

        # Test ticket price sorting
        ticket = Ticket(15.0)
        event.add_ticket(ticket)
        ticket = Ticket(14.0)
        event.add_ticket(ticket)
        ticket = event.get_cheapest_ticket()
        self.assertEqual(ticket.price, 14.0)

if __name__ == '__main__':
    unittest.main()
