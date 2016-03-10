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
    
    def simulate(self, moves):
        for move in moves:
            if move == 'L':
                self.turn_left()
            elif move == 'R':
                self.turn_right()
            elif move == 'A':
                self.advance()

    
    