from factorial import factorial
from fibonacci import fibonacci
from vowels import count_vowels
from prime_number import prime_number
from find_max import find_max
def main():
    n = 5
    print(factorial(n)) #рекурсивная функция для нахождения факториала числа

    fib_n = 10
    print(fibonacci(fib_n)) #рекурсивная функция для нахождения N-Го числа Фибоначи

    print(count_vowels('Hello uOu hi hi hi')) #подсчет гласных букв

    n2 = 2
    print(prime_number(n2)) #рекурсивная функция для определения является ли число простым

    print(find_max([1, 2, 3, 4, 5, 6, 7])) #рекурсивная функция для нахождения максимального числа


if __name__ == "__main__":
    main()
