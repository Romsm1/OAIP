class Stick:
    def __init__(self):
        self.name = "Stick"
    
    def info(self):
        return f"Material: {self.name}"

class Wood:
    def __init__(self):
        self.name = "Wood"
    
    def info(self):
        return f"Material: {self.name}"

class Cobblestone:
    def __init__(self):
        self.name = "Cobblestone"
    
    def info(self):
        return f"Material: {self.name}"

class IronIngot:
    def __init__(self):
        self.name = "Iron Ingot"
    
    def info(self):
        return f"Material: {self.name}"

class Diamond:
    def __init__(self):
        self.name = "Diamond"
    
    def info(self):
        return f"Material: {self.name}"

class Sword:
    def __init__(self, material, durability, damage):
        self.material = material
        self.durability = durability
        self.damage = damage
    
    def info(self):
        return f"Sword made of {self.material.name}, Durability: {self.durability}, Damage: {self.damage}"

class Pickaxe:
    def __init__(self, material, durability, efficiency):
        self.material = material
        self.durability = durability
        self.efficiency = efficiency
    
    def info(self):
        return f"Pickaxe made of {self.material.name}, Durability: {self.durability}, Efficiency: {self.efficiency}"

def craft_sword(stick_count, material_count, material):
    if stick_count >= 1 and material_count >= 2:
        durability = {"Wood": 59, "Cobblestone": 131, "Iron Ingot": 250, "Diamond": 1561}[material.name]
        damage = {"Wood": 4, "Cobblestone": 5, "Iron Ingot": 6, "Diamond": 7}[material.name]
        return Sword(material, durability, damage)
    else:
        return "Not enough materials!"

def craft_pickaxe(stick_count, material_count, material):
    if stick_count >= 2 and material_count >= 3:
        durability = {"Wood": 59, "Cobblestone": 131, "Iron Ingot": 250, "Diamond": 1561}[material.name]
        efficiency = {"Wood": 2, "Cobblestone": 4, "Iron Ingot": 6, "Diamond": 8}[material.name]
        return Pickaxe(material, durability, efficiency)
    else:
        return "Not enough materials!"

while True:
    item_type = input("Craft sword or pickaxe? (sword/pickaxe/exit): ")
    if item_type == "exit":
        break
    material_name = input("Choose material (Wood, Cobblestone, Iron Ingot, Diamond): ")
    stick_count = int(input("Enter number of sticks: "))
    material_count = int(input(f"Enter number of {material_name}: "))
    
    if material_name not in ["Wood", "Cobblestone", "Iron Ingot", "Diamond"]:
        print("Invalid material!")
        continue
    
    material = globals()[material_name.replace(" ", "")]()
    
    if item_type == "sword":
        item = craft_sword(stick_count, material_count, material)
    elif item_type == "pickaxe":
        item = craft_pickaxe(stick_count, material_count, material)
    else:
        print("Invalid choice!")
        continue
    
    if isinstance(item, str):
        print(item)
    else:
        print(item.info())
