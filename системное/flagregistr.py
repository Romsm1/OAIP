class FlagsRegister:
    def __init__(self):
        self.zero = False  # флаг нулевого результата (Z)
        self.negative = False  # флаг отрицательного результата (N)
        self.overflow = False  # флаг переполнения (O)

    def update(self, value: list):
        int_value = int("".join(map(str, value)), 2)  # преобразование списка битов в целое число

        self.zero = int_value == 0
        self.negative = False

        self.overflow = int_value >= (2 ** 32 - 1)
        self.load(int_value % )
