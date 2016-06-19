import random as r

ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
used_names = []

class Robot:
    def __init__(self):
        self.generate_name()
    
    def reset(self):
        self.generate_name()
        
    def generate_name(self):
        name = r.choice(ABC) + r.choice(ABC) + '{0:03d}'.format(r.randrange(0,999))
        if name in used_names:
            self.generate_name()
        else:
            used_names.append(name)
            self.name = name
            