class Pet:
    def __init__(self, name="Имя питомца"):
        self.name = name
        self.hunger = 50
        self.happy = 50
        self.sleep = 50
        self.hygiene = 50

    def feed(self):
        if self.hunger >= 50:
            print(f"{self.name} голоден, его нужно покормить")



