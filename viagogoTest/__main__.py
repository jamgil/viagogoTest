from .constants import X_LIMIT, Y_LIMIT
from .coordinate import Coordinate
from .grid import Grid


def main():
    user_input = input("Enter your coordinate in the form of 'x,y' (without quotations): ")

    # Some very basic input validation
    coord_input = [int(s) for s in user_input.split(',') if s.isdigit()]
    if len(coord_input) != 2 or not (X_LIMIT[0] <= coord_input[0] <= X_LIMIT[1] and
                                     Y_LIMIT[0] <= coord_input[1] <= Y_LIMIT[1]):
        print("Your input was invalid - please try again (example: 3,4)")
    else:
        grid = Grid()
        coord = Coordinate(coord_input[0], coord_input[1])
        grid.populate_grid_random_data()
        events = grid.get_nearest_events(coord, 5)
        for event in events:
            print(f"{event[0]} - ${event[0].get_cheapest_ticket().price}, Distance {event[1]}")

if __name__ == '__main__':
    main()
