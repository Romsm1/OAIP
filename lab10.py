class Stick:
    def __init__(self):
        self.__name = "Палка"

    def get_name(self):
        return self.__name

    def info(self):
        return f"Материал: {self.__name}"


class Wood:
    def __init__(self):
        self.__name = "Дерево"

    def get_name(self):
        return self.__name

    def info(self):
        return f"Материал: {self.__name}"


class Stone:
    def __init__(self):
        self.__name = "Камень"

    def get_name(self):
        return self.__name

    def info(self):
        return f"Материал: {self.__name}"


class Iron:
    def __init__(self):
        self.__name = "Железо"

    def get_name(self):
        return self.__name

    def info(self):
        return f"Материал: {self.__name}"


class Diamond:
    def __init__(self):
        self.__name = "Алмаз"

    def get_name(self):
        return self.__name

    def info(self):
        return f"Материал: {self.__name}"


class Sword:
    def __init__(self, material_name, durability, damage):
        self.__material_name = material_name
        self.__durability = durability
        self.__damage = damage

    def get_material_name(self):
        return self.__material_name

    def get_durability(self):
        return self.__durability

    def get_damage(self):
        return self.__damage

    def info(self):
        return f"Меч из {self.__material_name}, Прочность: {self.__durability}, Урон: {self.__damage}"


class Pickaxe:
    def __init__(self, material_name, durability, efficiency):
        self.__material_name = material_name
        self.__durability = durability
        self.__efficiency = efficiency

    def get_material_name(self):
        return self.__material_name

    def get_durability(self):
        return self.__durability

    def get_efficiency(self):
        return self.__efficiency

    def info(self):
        return f"Кирка из {self.__material_name}, Прочность: {self.__durability}, Эффективность: {self.__efficiency}"


class EnchantedSword:
    def __init__(self, material_name, durability, damage):
        self.__material_name = material_name
        self.__durability = durability
        self.__base_damage = damage
        self.__enchantment = "Острота"
        self.__enchanted_damage = damage + 3

    def info(self):
        return f"Зачарованный меч из {self.__material_name}, Прочность: {self.__durability}, Базовый урон: {self.__base_damage}, Зачарование: {self.__enchantment}, Новый урон: {self.__enchanted_damage}"


class EnchantedPickaxe:
    def __init__(self, material_name, durability, efficiency):
        self.__material_name = material_name
        self.__durability = durability
        self.__base_efficiency = efficiency
        self.__enchantment = "Efficiency"
        self.__enchanted_efficiency = efficiency + 2

    def info(self):
        return f"Зачарованная кирка из {self.__material_name}, Прочность: {self.__durability}, Базовая эффективность: {self.__base_efficiency}, Защита: {self.__enchantment}, Новая эффективность: {self.__enchanted_efficiency}"


class Forge:
    def craft_sword(self, stick_count, material_count, material):
        if stick_count >= 1 and material_count >= 2:
            material_name = material.get_name()
            durability = {"Дерево": 59, "Камень": 131, "Железо": 250, "Алмаз": 1561}.get(material_name)
            damage = {"Дерево": 4, "Камень": 5, "Железо": 6, "Алмаз": 7}.get(material_name)
            if durability is None or damage is None:
                return "Недопустимый материал!"
            return Sword(material_name, durability, damage)
        else:
            return "Недостаточно материалов!"

    def craft_pickaxe(self, stick_count, material_count, material):
        if stick_count >= 2 and material_count >= 3:
            material_name = material.get_name()
            durability = {"Дерево": 59, "Камень": 131, "Железо": 250, "Алмаз": 1561}.get(material_name)
            efficiency = {"Дерево": 2, "Камень": 4, "Железо": 6, "Алмаз": 8}.get(material_name)
            if durability is None or efficiency is None:
                return "Недопустимый материал!"
            return Pickaxe(material_name, durability, efficiency)
        else:
            return "Недостаточно материалов!"


class Anvil:
    def upgrade(self, item, material):
        material_name = material.get_name()
        if isinstance(item, Sword):
            item._Sword__durability += {"Дерево": 5, "Камень": 10, "Железо": 100, "Алмаз": 300}.get(material_name)
            item._Sword__damage += {"Дерево": 1, "Камень": 2, "Железо": 3, "Алмаз": 4}.get(material_name)
        elif isinstance(item, Pickaxe):
            item._Pickaxe__durability += {"Дерево": 5, "Камень": 10, "Железо": 100, "Алмаз": 300}.get(material_name)
            item._Pickaxe__efficiency += {"Дерево": 1, "Камень": 2, "Железо": 3, "Алмаз": 4}.get(material_name)
        else:
            return "Недопустипый тип предмета!"
        return item

    def __add__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            item, material = other
            self.upgrade(item, material)
            return item


class Workbench:
    def disassemble(self, item):
        if isinstance(item, Sword):
            material_name = item.get_material_name()
            return material_name
        elif isinstance(item, Pickaxe):
            material_name = item.get_material_name()
            return material_name
        else:
            return "Недопустимый тип предмета!"

    def __add__(self, other):
        if isinstance(other, (Sword, Pickaxe)):
            return self.disassemble(other)


forge = Forge()
anvil = Anvil()
workbench = Workbench()

materials = {
    "Дерево": Wood(),
    "Камень": Stone(),
    "Железо": Iron(),
    "Алмаз": Diamond()
}

while True:
    item_type = input("Создать меч или кирку? (Меч/Кирка/Выход): ")
    if item_type == "Выход":
        break

    material_name = input("Выберите материал (Дерево, Камень, Железо, Алмаз): ")
    if material_name not in materials:
        print("Неверный материал!")
        continue

    stick_count = int(input("Введите количество палок: "))
    material_count = int(input(f"Введите количество {material_name}: "))

    material = materials.get(material_name)

    if item_type == "Меч":
        item = forge.craft_sword(stick_count, material_count, material)
    elif item_type == "Кирка":
        item = forge.craft_pickaxe(stick_count, material_count, material)
    else:
        print("Неверный выбор!")
        continue

    if isinstance(item, str):
        print(item)
    else:
        enchant = input("Хотите зачаровать? (Да/Нет): ")
        if enchant == "Да":
            if isinstance(item, Sword):
                enchanted_item = EnchantedSword(
                    item.get_material_name(),
                    item.get_durability(),
                    item.get_damage()
                )
            elif isinstance(item, Pickaxe):
                enchanted_item = EnchantedPickaxe(
                    item.get_material_name(),
                    item.get_durability(),
                    item.get_efficiency()
                )
            print(enchanted_item.info())
        else:
            print(item.info())

        # Улучшение с помощью наковальни
        upgrade_choice = input("Хотите улучшить предмет на наковальне? (Да/Нет): ")
        if upgrade_choice == "Да":
            upgrade_material_name = input("Выберите материал для улучшения (Дерево, Камень, Железо, Алмаз): ")
            if upgrade_material_name not in materials:
                print("Неверный материал!")
                continue

            upgrade_material = materials.get(upgrade_material_name)
            upgraded_item = anvil + (item, upgrade_material)
            print("Предмет улучшен!")
            print(upgraded_item.info())

        # Разборка предмета
        disassemble_choice = input("Хотите разобрать предмет? (Да/Нет): ")
        if disassemble_choice == "Да":
            material = workbench + item
            print(f"Предмет разобран. Ресурсы которые были получены: {material}")
