# Задание 1
def main():
    try:
        num1 = int(input("Введите первое целое число: "))
        num2 = int(input("Введите второе целое число: "))
        result = num1 + num2
        print(f"Результат сложения: {result}")
    
    except ValueError:
    # Обработка ошибки  если введены не    целые числа
        print("Ошибка: введены не целые числа. ")

# Задание 2
    while True:
        try:
            num1 = int(input("Введите первое целое число: "))
            num2 = int(input("Введите второе целое число: "))
        
            result = num1 + num2
            print(f"Результат сложения: {result}")
            break
        
         except ValueError:
            print("Ошибка: введены нецелые числа. Пожалуйста, введите целые числа.")

# Задание 3
    while True:
        try:
            num1 = int(input("Введите первое целое число: "))
            num2 = int(input("Введите второе целое число: "))     
            result = num1 / num2
            print(f"Результат деления: {result}")
        
            break
        except ValueError:
            print("Ошибка: введены нецелые числа.")
        except ZeroDivisionError as a:
        # Обработка ошибки деления на 0
            print(a)
# Задание 4
    while True:
        try:
            num1 = int(input("Введите первое целое число: "))
            num2 = int(input("Введите второе целое число: "))
        
            sum_result = num1 + num2
            print(f"Результат сложения: {sum_result}")
            div_result = num1 / num2
            print(f"Результат деления: {div_result}")
        
            break
        except ValueError:
            print("Ошибка: введены нецелые числа. ")
        except ZeroDivisionError as a:
            print(a)
# Задание 5
    while True:
        try:
            num1 = int(input("Введите первое целое число: "))
            num2 = int(input("Введите второе целое число: "))
       
            sum_result = num1 + num2
        
            div_result = num1 / num2
            print(f"Результат деления: {div_result}")
        
            break
        except ValueError:
            print("Ошибка: введены нецелые числа.")
        except ZeroDivisionError as e:
            print(e)
        finally:
            print("Выход из программы")


if __name__ == '__main__':
    main()
