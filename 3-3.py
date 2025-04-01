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