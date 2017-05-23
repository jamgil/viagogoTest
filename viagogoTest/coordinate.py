class Coordinate(object):
    """ This class represents coordinate points on a 2d grid """

    def __init__(self, x, y, event=None):
        self._x = x
        self._y = y
        # Store a singular event due to project restriction
        self._event = event

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    @property
    def event(self):
        return self._event

    @event.setter
    def event(self, event):
        self._event = event
