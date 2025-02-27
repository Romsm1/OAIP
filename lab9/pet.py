class Pet:
    def __init__(self, name="Имя питомца"):
        self.name = name
        self.hunger = 50
        self.happy = 50
        self.sleeping = False
        self.sleepiness = 50
        self.hygiene = 80

    def eat(self):
        if self.hunger >= 50:
            self.hunger -= 30
            self.happy += 10
            self.hygiene -= 10
            self.sleepiness -= 5
            print(f"\n{self.name} поел и чувствует себя лучше, но немного испачкался.")
        else:
            print(f"\n{self.name} не голоден.")

        self.hunger = min(100, self.hunger)
        self.happy = min(100, self.happy)
        self.hygiene = min(100, self.hygiene)

    def sleep(self):
        if not self.sleeping:
            self.sleeping == True
            print(f"\n{self.name} лег спать.")

    def not_sleep(self):
        self.sleeping == False
        self.happy += 15
        self.hunger += 20
        self.sleepiness -= 50
        print(f"\nПока спал {self.name} его счастье повысилось, а голод увеличился. ")

        self.hunger = min(100, self.hunger)
        self.happy = min(100, self.happy)
        self.sleepiness = max(100, self.sleepiness)

    def shower(self):
        if self.hygiene <= 90:
            self.hygiene += 30
            self.happy += 5
            self.sleepiness -= 1
            print(f"\n{self.name} принял душ.")
        else:
            print(f"\n{self.name} чист и не хочет принимать душ.")
        self.happy = min(100, self.happy)
        self.sleepiness = max(100, self.sleepiness)
        self.hygiene = min(100, self.hygiene)

    def buy_item(self):
        self.happy += 30
        print(f"\n{self.name} доволен вашим подарком!")

        self.happy = min(100, self.happy)

    def show_status(self):
        print(
            f"\nИмя: {self.name}, его показатели = Голод: {self.hunger}, Счастье: {self.happy}, Гигиена: {self.hygiene}, Сонливость: {self.sleepiness}")
