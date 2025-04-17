class Chest:
    def __init__(self):
        # инициализация сундука с пустым содержимым и закрытым состоянием
        self.contents = []
        self.opened = False

    def open(self):
        # метод открытия сундука
        if not self.opened:
            print("Сундук открыт!")
            self.opened = True
        else:
            print("Сундук уже открыт.")

    def close(self):
        # метод закрытия сундука
        if self.opened:
            print("Сундук закрыт!")
            self.opened = False
        else:
            print("Сундук уже закрыт.")

    def add_item(self, item):
        # метод добавления в сундук предметов
        if self.opened:
            self.contents.append(item)
            print(f"Предмет: '{item}' добавлен в сундук.")
        else:
            print("Невозможно положить предмет, сундук закрыт!")

    def remove_item(self, item):
        # метод удаления предмета из сундука
        if self.opened:
            if item in self.contents:
                self.contents.remove(item)
                print(f"Предмет: '{item}' был удален из сундука.")
            else:
                print(f"Предмет: '{item}' не был найден в сундуке.")
        else:
            print("Нельзя удалить предмет, сундук закрыт!")

    def show_content(self):
        # метод показа содержимого
        if self.opened:
            if self.contents:
                print("Содержимое сундука: ")
                for item in self.contents:
                    print(f"{item}")
            else:
                print("Сундук пуст.")
        else:
            print("Нельзя увидеть содержимое, сундук закрыт!")
