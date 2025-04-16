class Button:
    def __init__(self, text="Нажми меня", color="green", size="medium", shape="oval", x=0, y=0):
        self.text = text
        self.color = color
        self.size = size
        self.shape = shape
        self.pressed = False
        self.click_count = 0
        self.x = x
        self.y = y

    def show_properties(self):
        # свойства кнопки
        print(f"Текст кнопки = '{self.text}', Цвет = '{self.color}', Размер = '{self.size}', Форма = '{self.shape}'")
         

    def press(self):
        # метод нажатия кнопки
        if not self.pressed:
            print(f"Кнопка: '{self.text}' была нажата.")
            self.pressed = True
            self.click_count += 1
        else:
            print(f"Кнопка: '{self.text}' уже нажата.")

    def release(self):
        # метод для отпускания кнопки
        if self.pressed:
            print(f"Кнопка: '{self.text}' была отжата.")
            self.pressed = False
        else:
            print(f"Кнопка: '{self.text}' не была нажата.")

    def hold(self):
        # зажатие кнопки
        if not self.pressed:
            print(f"Кнопка: '{self.text}' кнопка зажата.")
            self.pressed = True
            self.click_count += 1
        else:
            print(f"Кнопка: '{self.text}' уже зажата.")

    def click_multiple_times(self, times):
        # сколько раз была нажата кнопка
        for _ in range(times):
            self.press()
            self.release()

    def display_clicks(self):
        if self.click_count == 1:
            print(f"Кнопка: '{self.text}' была нажата 1 раз.")
        else:
            print(f"Кнопка: '{self.text}' была нажата {self.click_count} раз.")