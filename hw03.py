# Task 3.1.
# Calculates the number of days between a given date and the current date
from datetime import datetime, date


def get_days_from_today(date_str):
    """
    Розраховує кількість днів між заданою датою та поточною датою.

    Args:
        date_str (str): Рядок, що представляє дату у форматі 'РРРР-ММ-ДД'.

    Returns:
        int: Кількість днів від заданої дати до поточної.
    """
    try:
        given_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        current_date = date.today()
        days_past = (current_date - given_date).days
        return days_past
    except ValueError:
        return "Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'."
    except TypeError:
        return "Неправильний тип даних. Введіть рядок"


# Приклад використання функції
date_string = '2014-03-20'
days_past = get_days_from_today(date_string)
print(f"Між заданою датою і поточною датою минуло днів: {days_past}")  # Виведеться різниця в днях

date_string = '2024.13.20'
days_past = get_days_from_today(date_string)
print(days_past)

date_string = 2024
days_past = get_days_from_today(date_string)
print(days_past)

# _________________________________________________
# Task 3.2.
# Generates a set of unique random numbers within the specified parameters
import random

def get_numbers_ticket(min_num, max_num, quantity):
    """
    Генерує випадковий набір унікальних чисел для лотереї.

    Args:
        min_num (int): Мінімальне можливе число у наборі (не менше 1).
        max_num (int): Максимальне можливе число у наборі (не більше 1000).
        quantity (int): Кількість чисел, які потрібно вибрати (значення між min та max).

    Returns:
        list: Відсортований список випадково вибраних унікальних чисел.
              Повертає пустий список, якщо параметри не відповідають заданим обмеженням.
    """

    if not isinstance(min_num, int) or not isinstance(max_num, int) or not isinstance(quantity, int):
        return []

    if min_num < 1 or max_num > 1000 or quantity < 1 or quantity > (max_num - min_num + 1):
        return []

    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min_num, max_num))

    return sorted(list(numbers))

# Приклад використання функції
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 36, 5)
print("Ваші лотерейні числа:", lottery_numbers)

# _________________________________________________
# Task 3.3.
# Normalizes phone numbers to a standard format
import re

def normalize_phone(phone_number):
    """
    Нормалізує телефонні номери до стандартного формату.

    Args:
        phone_number (str): Рядок з телефонним номером у будь-якому форматі.

    Returns:
        str: Нормалізований телефонний номер.
    """

    # Видаляємо всі символи, крім цифр та '+'
    cleaned_number = re.sub(r'[^\d+]', '', phone_number)

    # Перевіряємо, чи номер починається з '+'
    if cleaned_number.startswith('+'):
        # Якщо так, перевіряємо, чи є код країни
        if cleaned_number.startswith('+380'):
            return cleaned_number  # Номер вже в правильному форматі
        else:
            return '+38' + cleaned_number[1:]  # Додаємо код України
    else:
        # Якщо номер не починається з '+', додаємо код України
        return '+38' + cleaned_number

# Приклад використання функції
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

# _________________________________________________
