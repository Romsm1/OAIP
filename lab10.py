class Stick:
    def __init__(self):
        self.__name = "Палка"

    def get_name(self):
        return self.__name

    def info(self):
        return f"Материал: {self.__name}"


class Material:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def info(self):
        return f"Материал: {self.__name}"


class Wood(Material):
    def __init__(self):
        super().__init__("Дерево")


class Stone(Material):
    def __init__(self):
        super().__init__("Камень")


class Iron(Material):
    def __init__(self):
        super().__init__("Железо")


class Diamond(Material):
    def __init__(self):
        super().__init__("Алмаз")


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
    def __init__(self, sword_material, sword_durability, sword_damage):
        self.__sword_material = sword_material
        self.__sword_durability = sword_durability
        self.__sword_damage = sword_damage
        self.__enchantment = "Острота V"

    def info(self):
        return f"Меч из {self.__sword_material}, Прочность: {self.__sword_durability}, Урон: {self.__sword_damage}, Защита: {self.__enchantment}"


class EnchantedPickaxe:
    def __init__(self, pickaxe_material, pickaxe_durability, pickaxe_efficiency):
        self.__pickaxe_material = pickaxe_material
        self.__pickaxe_durability = pickaxe_durability
        self.__pickaxe_efficiency = pickaxe_efficiency
        self.__enchantment = "Шелковое касание III"

    def info(self):
        return f"Кирка из {self.__pickaxe_material}, Прочность: {self.__pickaxe_durability}, Эффективность: {self.__pickaxe_efficiency}, Защита: {self.__enchantment}"


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


# Главный цикл программы
forge = Forge()

materials = {
    "Дерево": Wood(),
    "Камень": Stone(),
    "Железо": Iron(),
    "Алмаз": Diamond()
}

while True:
    item_type = input("Создать меч или кирку? (Меч/Кирка/Выход): ").strip().capitalize()
    if item_type == "Выход":
        break

    material_name = input("Выберите материал (Дерево, Камень, Железо, Алмаз): ").strip().capitalize()
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
        enchant = input("Хотите зачаровать? (Да/Нет): ").strip().lower()
        if enchant == "да":
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