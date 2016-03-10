from _collections import OrderedDict
[NORTH, EAST, SOUTH, WEST] = [1,2,3,4]

class Robot:
    def __init__(self, bearing = NORTH, x = 0, y = 0):
        self.coordinates = (x,y)
        self.bearing = bearing
    
    def turn_left(self):
        self.bearing = self.bearing - 1
        if self.bearing < NORTH:
            self.bearing = WEST
            
    def turn_right(self):
        self.bearing = self.bearing + 1
        if self.bearing > WEST:
            self.bearing = NORTH
    
    def advance(self):
        (x, y) = self.coordinates
        if self.bearing == NORTH:
            y += 1
        elif self.bearing == SOUTH:
            y -= 1
        elif self.bearing == WEST:
            x -= 1
        else:
            x += 1
        self.coordinates = (x, y)
    
    def alter_coord(self, coord_index, delta):
        self.coordinates[coord_index] += delta

    def simulate(self, moves):
        possible_moves = {'L':self.turn_left, 'R':self.turn_right, 'A':self.advance}
        for move in moves:
            possible_moves[move]()

    
    