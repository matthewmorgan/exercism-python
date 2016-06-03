SECONDS_PER_YEAR_ON_EARTH = 31557600

CONVERSIONS = {
    'earth': 1,
    'mercury': .2408467,
    'venus': .61519726,
    'mars': 1.88087158,
    'jupiter': 11.862615,
    'saturn': 29.447498,
    'uranus': 84.016846,
    'neptune': 164.79132
}


class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds


def factory(planet_name):
    def function(self):
        return float(format(self.seconds / CONVERSIONS[planet_name] / SECONDS_PER_YEAR_ON_EARTH, '.2f'))
    return function

for planet_name in CONVERSIONS:
    setattr(SpaceAge, 'on_'+planet_name, factory(planet_name))





