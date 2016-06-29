KINDS = ['equilateral', 'isosceles', 'scalene']


class Triangle:
    def __init__(self, *args):
        self.sides = sorted(args)
        self._raise_if_illegal()

    def kind(self):
        return KINDS[len(set(self.sides))-1]

    def _raise_if_illegal(self):
        if self.sides[2] >= self.sides[1] + self.sides[0]:
            raise TriangleError
        if any(side <= 0 for side in self.sides):
            raise TriangleError


class TriangleError(Exception):
    pass
