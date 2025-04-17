class Button:
    def __init__(self, text="Нажми меня", color="green", width=100, height=50, shape="oval", x=0, y=0):
        # Инициализация свойств кнопки
        self.text = text
        self.color = color
        self.width = width  # Ширина в пикселях
        self.height = height  # Высота в пикселях
        self.shape = shape
        self.pressed = False
        self.click_count = 0
        self.x = x
        self.y = y

    def show_properties(self):
        # Отображение свойств кнопки
        print(f"Текст кнопки = '{self.text}', Цвет = '{self.color}', Размер = {self.width}x{self.height} пикселей, Форма = '{self.shape}'")
        print(f"Координаты кнопки: X = {self.x}, Y = {self.y}")

    def press(self):
        # Метод нажатия кнопки
        if not self.pressed:
            print(f"Кнопка: '{self.text}' была нажата.")
            self.pressed = True
            self.click_count += 1
        else:
            print(f"Кнопка: '{self.text}' уже нажата.")

    def release(self):
        # Метод отпускания кнопки
        if self.pressed:
            print(f"Кнопка: '{self.text}' была отжата.")
            self.pressed = False
        else:
            print(f"Кнопка: '{self.text}' не была нажата.")

    def hold(self):
        # Зажатие кнопки
        if not self.pressed:
            print(f"Кнопка: '{self.text}' кнопка зажата.")
            self.pressed = True
            self.click_count += 1
        else:
            print(f"Кнопка: '{self.text}' уже зажата.")

    def click_multiple_times(self, times):
        # Многократное нажатие кнопки
        for _ in range(times):
            self.press()
            self.release()

    def display_clicks(self):
        # Отображение количества нажатий
        if self.click_count == 1:
            print(f"Кнопка: '{self.text}' была нажата 1 раз.")
        else:
            print(f"Кнопка: '{self.text}' была нажата {self.click_count} раз.")

    def edit_properties_interactive(self):
        """
        Метод для интерактивного редактирования свойств кнопки через input().
        """
        print("Введите новые значения для свойств кнопки (оставьте пустым, чтобы оставить текущее значение):")

        # Текст
        new_text = input(f"Текущий текст кнопки: '{self.text}'. Введите новый текст: ")
        if new_text.strip():  # Если пользователь ввел что-то
            self.text = new_text

        # Цвет
        new_color = input(f"Текущий цвет кнопки: '{self.color}'. Введите новый цвет: ")
        if new_color.strip():
            self.color = new_color

        # Ширина
        new_width = input(f"Текущая ширина кнопки: {self.width} пикселей. Введите новую ширину: ")
        if new_width.strip() and new_width.isdigit():  # Проверяем, что введено число
            self.width = int(new_width)

        # Высота
        new_height = input(f"Текущая высота кнопки: {self.height} пикселей. Введите новую высоту: ")
        if new_height.strip() and new_height.isdigit():
            self.height = int(new_height)

        # Форма
        new_shape = input(f"Текущая форма кнопки: '{self.shape}'. Введите новую форму: ")
        if new_shape.strip():
            self.shape = new_shape

        # Координата X
        new_x = input(f"Текущая координата X кнопки: {self.x}. Введите новую координату X: ")
        if new_x.strip() and new_x.isdigit():
            self.x = int(new_x)

        # Координата Y
        new_y = input(f"Текущая координата Y кнопки: {self.y}. Введите новую координату Y: ")
        if new_y.strip() and new_y.isdigit():
            self.y = int(new_y)

        print("Свойства кнопки были обновлены.")