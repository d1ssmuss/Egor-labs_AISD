"""
Лабораторная работа №2
Написать программу, решающую задачу из 1 лабораторной работы (в соответствии со своим вариантом) со следующими изменениями:
1.  Входной файл является обыкновенным (т.е. нет требования на «бесконечность» файла);
2.  Распознавание и обработку делать  через регулярные выражения;
3.  В вариантах, где есть параметр (например К), допускается его заменить на любое число;
4.  Все остальные требования соответствуют варианту задания лабораторной работы №1.
Вариант 23.
Натуральные четные числа, начинающиеся с нечетной цифры и содержащие не более 3 нечетных цифр.
Для каждого числа через тире вывести прописью первую цифру и нечетные цифры.
"""
import re

# Функция для перевода цифр в слова
def digit_to_word(digit):
    words = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    return words[int(digit)]

def process_numbers(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # Находим все числа в тексте, игнорируя буквы и другие символы
    numbers = re.findall(r'\d+', content)

    # Паттерн для проверки четных чисел, начинающихся с нечетной цифры
    pattern = re.compile(r'^[13579]\d*[02468]$')

    for number in numbers:
        number = number.strip()

        if pattern.match(number) and len(re.findall(r'[13579]', number)) <= 3:
            odd_digits = re.findall(r'[13579]', number)
            first_digit = digit_to_word(number[0])
            odd_digits_words = " - ".join(digit_to_word(digit) for digit in odd_digits)
            print(f"Число {number}: {first_digit} - {odd_digits_words}")

if __name__ == "__main__":
    process_numbers('Егор/23.txt')