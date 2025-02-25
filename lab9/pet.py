class Pet:
    def __init__(self, name="Имя питомца"):
        self.name = name
        self.hunger = 50
        self.happy = 50
        self.sleep = False
        self.sleepiness = 50
        self.hygiene = 50

    def feed(self):
        if self.hunger <= 50:
            self.hunger -= 30
            self.happy += 10
            self.hygiene -= 10
            print(f"{self.name} поел и чувствует себя лучше, но немного испачкался.")
        else:
            print(f"{self.name} не голоден.")

    def sleep(self):
        self.sleep() == True
        print(f"{self.name} спит.")

    def not_sleep(self):
        self.sleep() == False
        print(f"{self.name} проснулся.")

    def sleep_status(self):
        if self.sleep():
            self.happy += 15
            self.hunger -= 20
            self.sleepiness -= 50
            print(f"Пока спал {self.name} его счастье повысилось, а голод увеличился. ")

    def shower(self):
        self.hygiene += 20
        self.happy += 5
        self.sleepiness -= 5
        print(f"{self.name} принял душ.")

    def show_status(self):
        print(f"Имя: {self.name}, его показатели = Голод: {self.hunger}, Счастье: {self.happy}, Гигиена: {self.hygiene}, Сонливость: {self.sleepiness}")