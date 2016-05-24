GRADE_LEVELS = 9


class School:
    def __init__(self, school_name):
        self.db = list(map(lambda x: [], [None] * GRADE_LEVELS))

    def grade(self, grade):
        return self.db[grade][:]

    def add(self, name, grade):
        self.db[grade].append(name)

    def sort(self):
        return [(i, tuple(self.db[i])) for i in range(1,len(self.db)) if self.db[i]]
