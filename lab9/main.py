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
    test_button = Button("Подтверждение", "Зелёный", "Большая", "Прямоугольная")
    test_button.show_properties()

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

    # ПИТОМЕЦ
    my_pet = Pet("Tom")

    my_pet.feed()


if __name__ == '__main__':
    main()