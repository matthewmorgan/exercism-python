import math


class Clock():
    def __init__(self, h, m):
        self.normalize(h,m)

    def normalize(self, h, m):
        self.minutes = m + h * 60
        self.hours = math.floor(self.minutes/60) % 24
        self.minutes %= 60

    def __str__(self):
        return "%02d:%02d" % (self.hours, self.minutes)

    def add(self, delta_minutes):
        self.minutes += delta_minutes
        self.normalize(self.hours, self.minutes)
        return self

    def __eq__(self, other):
        return self.__str__() == other.__str__()
