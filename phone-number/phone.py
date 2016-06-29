class Phone:
    def __init__(self, raw):
        self.number = self._normalize(raw)

    def pretty(self):
        n = self.number
        return '({}) {}-{}'.format(n[:3], n[3:6], n[6:])

    def area_code(self):
        return self.number[:3]

    def _normalize(self, raw):
        number = ''.join([d for d in raw if d.isdigit()])
        if len(number) == 11 and number[0] == '1':
            number = number[1:]
        elif len(number) != 10:
            number = '0000000000'
        return number