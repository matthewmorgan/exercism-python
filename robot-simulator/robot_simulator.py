NORTH, EAST, SOUTH, WEST = 1, 2, 3, 4
BEARINGS = {NORTH: (0, 1), SOUTH: (0, -1), EAST: (1, 0), WEST: (-1, 0)}


class Robot:
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.coordinates = (x, y)
        self.bearing = bearing
        self.possible_moves = {'L': self.turn_left, 'R': self.turn_right, 'A': self.advance}

    def turn_left(self):
        self.bearing -= 1
        if self.bearing < NORTH:
            self.bearing = WEST

    def turn_right(self):
        self.bearing += 1
        if self.bearing > WEST:
            self.bearing = NORTH

    def advance(self):
        (dx, dy) = BEARINGS[self.bearing]
        (x, y) = self.coordinates
        self.coordinates = (x + dx, y + dy)

    def simulate(self, moves):
        for move in moves:
            self.possible_moves[move]()
            