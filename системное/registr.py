from flagregistr import FlagsRegister


class Register:
    def __init__(self, name: str, size: int = 32):
        self.name = name
        self.size = size
        self.value = [0] * size
        self.flags = FlagsRegister()

    def load(self, value: int):
        value = value % (2 ** 32)
        self.value = list(map(int, f"{value:0{self.size}b}"))

    def to_int(self):
        return int("".join(map(str, self.value)), 2)

    def add(self, other: 'Register') -> 'Register':
        result = self.to_int() + other.to_int()
        self.load(result)
        self.flags.update(self.value)

    def sub(self, other: 'Register') -> 'Register':
        result = max(0, self.to_int() - other.to_int())
        self.load(result)
        self.flags.update(self.value)

    def mul(self, other: 'Register') -> 'Register':
        result = self.to_int() * other.to_int()
        self.load(result % (2 ** 32))
        self.flags.update(self.value)

    def div(self, other: 'Register') -> 'Register':
        result = self.to_int() // other.to_int()
        self.load(result)
        self.flags.update(self.value)

    def __repr__(self):
        return f"Register({self.name}, Value={self.to_int()}, {self.flags})"
