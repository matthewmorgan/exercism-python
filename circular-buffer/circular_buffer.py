class CircularBuffer:
    def __init__(self, max_size):
        self.buffer = []
        self.max_size = max_size

    def read(self):
        if not self.buffer:
            raise BufferEmptyException
        return self.buffer.pop(0)

    def write(self, value):
        if len(self.buffer) == self.max_size:
            raise BufferFullException
        self.buffer.append(value)

    def overwrite(self, value):
        if len(self.buffer) == self.max_size:
            self.read()
        self.write(value)

    def clear(self):
        self.buffer = []


class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass
