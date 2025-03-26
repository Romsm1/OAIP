class Weapon:
    pass

class ColdWeapon(Weapon):
    pass

class Bladed(ColdWeapon):
    pass # Класс для клинкового оружия

class Piercing(Bladed):
    pass # Класс для колющего оружия

class Cutting(Bladed):
    pass # Класс для рубящего оружия

# Виды оружия в колющем:
class Forks(Piercing):
    pass # вилы

class Tridents(Piercing):
    pass # трезубцы

class Bayonets(Piercing):
    pass # штыки

class Swords(Piercing):
    pass # шпаги

class Stilettos(Piercing):
    pass # стилеты

class Daggers(Piercing):
    pass # кортики

# Виды оружия в рубящем:
class Shashkas(Cutting):
    pass # шашки

class Sabers(Cutting):
    pass # сабли

class Pikes(Cutting):
    pass # тесаки

class BattleAxe(Cutting):
    pass # боевые топоры

class Axes(Cutting):
    pass # секиры
