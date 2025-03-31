class Stick:
    def __init__(self):
        self.name = "Палка"
    
    def info(self):
        return f"Материал: {self.name}"

class Wood:
    def __init__(self):
        self.name = "Дерево"
    
    def info(self):
        return f"Материал: {self.name}"

class Stone:
    def __init__(self):
        self.name = "Камень"
    
    def info(self):
        return f"Материал: {self.name}"

class Iron:
    def __init__(self):
        self.name = "Железо"
    
    def info(self):
        return f"Материал: {self.name}"

class Diamond:
    def __init__(self):
        self.name = "Алмаз"
    
    def info(self):
        return f"Материал: {self.name}"

class Sword:
    def __init__(self, material, durability, damage):
        self.material = material
        self.durability = durability
        self.damage = damage
    
    def info(self):
        return f"Меч из {self.material.name}, Прочность: {self.durability}, Урон: {self.damage}"

class Pickaxe:
    def __init__(self, material, durability, efficiency):
        self.material = material
        self.durability = durability
        self.efficiency = efficiency
    
    def info(self):
        return f"Кирка из {self.material.name}, Прочность: {self.durability}, Эффективность: {self.efficiency}"

def craft_sword(stick_count, material_count, material):
    durability_dict = {"Дерево": 59, "Камень": 131, "Железо": 250, "Алмаз": 1561}
    damage_dict = {"Дерево": 4, "Камень": 5, "Железо": 6, "Алмаз": 7}
    
    if stick_count >= 1 and material_count >= 2:
        return Sword(material, durability_dict.get(material.name, 0), damage_dict.get(material.name, 0))
    else:
        return "Недостаточно материалов!"

def craft_pickaxe(stick_count, material_count, material):
    durability_dict = {"Дерево": 59, "Камень": 131, "Железо": 250, "Алмаз": 1561}
    efficiency_dict = {"Дерево": 2, "Камень": 4, "Железо": 6, "Алмаз": 8}
    
    if stick_count >= 2 and material_count >= 3:
        return Pickaxe(material, durability_dict.get(material.name, 0), efficiency_dict.get(material.name, 0))
    else:
        return "Недостаточно материалов!"

while True:
    item_type = input("Создать меч или кирку? (меч/кирка/выход): ")
    if item_type == "выход":
        break
    material_name = input("Выберите материал (Дерево, Камень, Железо, Алмаз): ")
    stick_count = int(input("Введите количество палок: "))
    material_count = int(input(f"Введите количество {material_name}: "))
    
    material_classes = {"Дерево": Wood, "Камень": Stone, "Железо": Iron, "Алмаз": Diamond}
    
    if material_name not in material_classes:
        print("Неверный материал!")
        continue
    
    material = material_classes[material_name]()
    
    if item_type == "меч":
        item = craft_sword(stick_count, material_count, material)
    elif item_type == "кирка":
        item = craft_pickaxe(stick_count, material_count, material)
    else:
        print("Неверный выбор!")
        continue
    
    if isinstance(item, str):
        print(item)
    else:
        print(item.info())
