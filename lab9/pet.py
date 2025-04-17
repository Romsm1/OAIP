class Pet:
    def __init__(self, name="Имя питомца"):
        self.name = name
        self.hunger = 50  
        self.happy = 50   
        self.hygiene = 80  
        self.sleepiness = 50  
        self.sleeping = False  
        self.alive = True  

    def normalize_stats(self):
        self.hunger = max(0, min(100, self.hunger))
        self.happy = max(0, min(100, self.happy))
        self.hygiene = max(0, min(100, self.hygiene))
        self.sleepiness = max(0, min(100, self.sleepiness))

    def check_alive(self):
        if self.hunger <= 0 or self.happy <= 0 or self.hygiene <= 0 or self.sleepiness >= 100:
            self.alive = False
            print(f"\n{self.name} умер... :(")

    def decrease_stats_while_waiting(self):
        if not self.sleeping:
            self.hunger -= 15
            self.happy -= 30
            self.hygiene -= 10
            self.sleepiness += 20
            print(f"\n{self.name} ждет. Его показатели ухудшились.")
        else:
            print(f"\n{self.name} спит. Показатели не меняются.")

    def eat(self):
        if not self.alive:
            print(f"\n{self.name} мертв и не может есть.")
            return

        if self.sleeping:
            print(f"\n{self.name} спит и не может есть.")
            return

        if self.hunger <= 50:
            self.hunger += 30
            self.happy += 10
            self.hygiene -= 10
            self.sleepiness -= 5
            print(f"\n{self.name} поел и чувствует себя лучше, но немного испачкался.")
        else:
            print(f"\n{self.name} не голоден.")

        self._normalize_stats()
        self._check_alive()

    def sleep(self):
        if not self.alive:
            print(f"\n{self.name} мертв и не может спать.")
            return

        if not self.sleeping:
            self.sleeping = True
            print(f"\n{self.name} лег спать.")
        else:
            print(f"\n{self.name} уже спит.")

    def not_sleep(self):
        if not self.alive:
            print(f"\n{self.name} мертв и не может проснуться.")
            return

        if self.sleeping:
            self.sleeping = False
            self.happy += 15
            self.hunger -= 25
            self.sleepiness -= 50
            print(f"\n{self.name} проснулся. Его счастье повысилось, а голод увеличился.")
        else:
            print(f"\n{self.name} и так не спит.")

        self._normalize_stats()
        self._check_alive()

    def shower(self):
        if not self.alive:
            print(f"\n{self.name} мертв и не может принимать душ.")
            return

        if self.sleeping:
            print(f"\n{self.name} спит и не может принимать душ.")
            return

        if self.hygiene <= 90:
            self.hygiene += 30
            self.happy += 5
            self.sleepiness -= 1
            print(f"\n{self.name} принял душ.")
        else:
            print(f"\n{self.name} чист и не хочет принимать душ.")

        self._normalize_stats()
        self._check_alive()

    def buy_item(self):
        if not self.alive:
            print(f"\n{self.name} мертв и не может получить подарок.")
            return

        if self.sleeping:
            print(f"\n{self.name} спит и не может получить подарок.")
            return

        self.happy += 30
        print(f"\n{self.name} доволен вашим подарком!")

        self._normalize_stats()
        self._check_alive()

    def show_status(self):
        if not self.alive:
            print(f"\n{self.name} мертв...")
            return

        status = (
            f"\nИмя: {self.name}\n"
            f"Голод: {self.hunger}\n"
            f"Счастье: {self.happy}\n"
            f"Гигиена: {self.hygiene}\n"
            f"Сонливость: {self.sleepiness}\n"
            f"Спит: {'Да' if self.sleeping else 'Нет'}"
        )
        print(status)

    def wait(self):
        if not self.alive:
            print(f"\n{self.name} мертв и не может ждать.")
            return
