from chest import Chest
from button import Button
from pet import Pet

def main():
    # СУНДУК
    chest_player = Chest()
    chest_player.open()

    chest_player.add_item("Зелье лечения")
    chest_player.add_item("Тяжёлые доспехи")
    chest_player.add_item("Двуручный меч")
    chest_player.add_item("Драгоценности")

    chest_player.show_content()

    chest_player.remove_item("Драгоценности")
    chest_player.remove_item("Зелье лечения")

    chest_player.show_content()
    chest_player.close()

    # КНОПКА
    print("\nСоздание кнопки:")
    text = input("Введите текст для кнопки (по умолчанию 'Нажми меня'): ") or "Нажми меня"
    color = input("Введите цвет кнопки (по умолчанию 'green'): ") or "green"

    # Ввод размера в пикселях
    try:
        width = int(input("Введите ширину кнопки в пикселях (по умолчанию 100): ") or 100)
        height = int(input("Введите высоту кнопки в пикселях (по умолчанию 50): ") or 50)
    except ValueError:
        print("Неверный формат размера. Будут использованы значения по умолчанию (100x50).")
        width, height = 100, 50

    shape = input("Введите форму кнопки (по умолчанию 'oval'): ") or "oval"

    # Ввод координат
    try:
        x = int(input("Введите координату X (по умолчанию 0): ") or 0)
        y = int(input("Введите координату Y (по умолчанию 0): ") or 0)
    except ValueError:
        print("Неверный формат координат. Будут использованы значения по умолчанию (0, 0).")
        x, y = 0, 0

    test_button = Button(text=text, color=color, width=width, height=height, shape=shape, x=x, y=y)
    test_button.show_properties()

    # Действия с кнопкой
    test_button.press()
    test_button.release()

    test_button.press()
    test_button.press()

    test_button.display_clicks()

    test_button.hold()
    test_button.release()

    clicks = int(input("Сколько раз нажать на кнопку?: "))
    test_button.click_multiple_times(clicks)
    print(f"Кнопка: '{test_button.text}' была нажата {test_button.click_count} раз")

    # Интерактивное редактирование кнопки
    edit_choice = input("Хотите изменить свойства кнопки? (да/нет): ").lower()
    if edit_choice == "да":
        test_button.edit_properties_interactive()
        print("Обновленные свойства кнопки:")
        test_button.show_properties()

    # ПИТОМЕЦ
    pet_name = input("Введите имя для вашего питомца: ")
    pet = Pet(pet_name)

    while True:
        print("\nМеню: ")
        print("Нажмите '1', чтобы показать статусы питомца.")
        print("Нажмите '2', чтобы покормить питомца.")
        print("Нажмите '3', чтобы питомец лег спать.")
        print("Нажмите '4', чтобы питомец проснулся.")
        print("Нажмите '5', чтобы питомец принял душ.")
        print("Нажмите '6', чтобы купить питомцу предмет.")
        print("Нажмите '7', чтобы выйти.")

        choice = input("\nВыберите какое действие нужно выполнить: ")
        if choice == "1":
            pet.show_status()
        elif choice == "2":
            pet.eat()
        elif choice == "3":
            pet.sleep()
        elif choice == "4":
            pet.not_sleep()
        elif choice == "5":
            pet.shower()
        elif choice == "6":
            pet.buy_item()
        elif choice == "7":
            break
        else:
            print("\nНажата неверная кнопка, повторите попытку!")

if __name__ == '__main__':
    main()