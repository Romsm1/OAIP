9class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self):
        print(f'{self.name} нанес удар силой: {self.attack_power}')

    def info(self):
        print(f'Имя: {self.name}, Здоровье: {self.hp}, Сила атаки: {self.attack_power}')


class Warrior(Character):
    def __init__(self, name, hp, attack_power, armor, endurance):
        super().__init__(name, hp, attack_power)
        self.armor = armor
        self.endurance = endurance

    def attack(self):
        if self.endurance >= 25:
            print(f'{self.name} наносит чистый урон размером: {self.attack_power}')
        else:
            print(f'У {self.name} недостаточно выносливости чтобы совершить удар!')

    def info(self):
        super().info()
        print(f'Броня: {self.armor}')
        print(f'Выносливость: {self.endurance}')


class Mage(Character):
    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp, attack_power)
        self.mana = mana

    def attack(self):
        if self.mana >= 20:
            print(f'{self.name} с помощью магии наносит магический урон размером: {self.attack_power}')
            self.mana -= 20
        else:
            print(f' У {self.name} недостаточно маны для использования магии!')

    def info(self):
        super().info()
        print(f'Мана: {self.mana}')


class Archer(Character):
    def __init__(self, name, hp, attack_power, arrows, endurance):
        super().__init__(name, hp, attack_power)
        self.endurance = endurance
        self.arrows = arrows

    def attack(self):
        if self.endurance >= 15 and self.arrows > 0:
            print(f'{self.name} стреляет из лука и наносит урон размером: {self.attack_power}')
        else:
            print(f'У {self.name} закончились стрелы либо недостаточно выносливости для совершения выстрела!')

    def info(self):
        super().info()
        print(f'Количество стрел: {self.arrows}')
        print(f'Выносливость: {self.endurance}')


warrior = Warrior("Воин", 100, 35, 50, 75)
warrior.info()
warrior.attack()

mage = Mage("Колдун", 78, 10, 45)
mage.info()
mage.attack()

archer = Archer("Лучник", 42, 15, 3, 45)
archer.info()
archer.attack()
