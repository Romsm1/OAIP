class Item:
    def __init__(self, name):
        self._name = name

    def get_info(self):
        return f"Предмет: {self._name}"

    def get_name(self):
        return self._name


class CraftingTable:
    def __init__(self):
        self._recipes = {
            ("Камень", "Камень", "Палка"): "Каменный меч",
            ("Доски", "Палка"): "Деревянный меч",
            ("Камень", "Камень", "Камень", "Палка", "Палка"): "Каменная кирка",
            ("Железо", "Железо", "Палка"): "Железный меч",
            ("Алмаз", "Алмаз", "Палка"): "Алмазный меч",
            ("Доски", "Доски", "Доски", "Палка", "Палка"): "Деревянная кирка",
            ("Железо", "Железо", "Железо", "Палка", "Палка"): "Железная кирка",
            ("Алмаз", "Алмаз", "Алмаз", "Палка", "Палка"): "Алмазная кирка"
        }

    def craft(self, items):
        item_names = tuple(sorted([item.get_name() for item in items]))
        print(f"Попытка крафта: {item_names}")
        if item_names in self._recipes:
            return Item(self._recipes[item_names])
        else:
            return None


# Ресурсы для крафта
stick = Item("Палка")
stone = Item("Камень")
wood = Item("Доски")
iron = Item("Железо")
diamond = Item("Алмаз")

# Создание верстака
table = CraftingTable()

# Крафт предметов
crafts = [
    ([stick, stone, stone], "Каменный меч"),
    ([wood, stick], "Деревянный меч"),
    ([stick, stick, stone, stone, stone], "Каменная кирка"),
    ([stick, iron, iron], "Железный меч"),
    ([stick, diamond, diamond], "Алмазный меч"),
    ([stick, stick, wood, wood, wood], "Деревянная кирка"),
    ([stick, stick, iron, iron, iron], "Железная кирка"),
    ([stick, stick, diamond, diamond, diamond], "Алмазная кирка")
]

for materials, expected in crafts:
    crafted_item = table.craft(materials)
    if crafted_item:
        print(crafted_item.get_info())
    else:
        print(f"Не удалось скрафтить {expected}")


