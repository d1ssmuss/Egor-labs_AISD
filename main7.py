"""
Сипатов Егор ИСТбд-23
Задание на л.р. №7
Требуется для своего варианта второй части л.р. №6 (усложненной программы) разработать реализацию с использованием графического интерфейса. Допускается использовать любую графическую библиотеку питона.
Рекомендуется использовать внутреннюю библиотеку питона  tkinter.
В программе должны быть реализованы минимум
одно окно ввода,
одно окно вывода (со скролингом),
одно текстовое поле,
одна кнопка.
"""
import tkinter as tk
from tkinter import scrolledtext, messagebox
from itertools import product


def distribute_items_with_constraints(T, K, max_items):
    return [distribution for distribution in product(range(min(max_items, T) + 1), repeat=K) if sum(distribution) == T]


def optimal_distribution(T, K, max_items):
    distributions = distribute_items_with_constraints(T, K, max_items)
    if not distributions:
        return None  # Если нет допустимых распределений
    optimal = min(distributions, key=lambda x: max(x) - min(x))
    return optimal


def calculate_distribution():
    try:
        T = int(entry_items.get())
        K = int(entry_people.get())
        max_items = int(entry_max_items.get())

        if T < 0 or K <= 0 or max_items < 0:
            raise ValueError("Параметры должны быть неотрицательными, а K - положительным.")

        optimal_result = optimal_distribution(T, K, max_items)

        if optimal_result is None:
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, "Нет допустимых распределений.")
        else:
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, f"Оптимальное распределение: {optimal_result}")

    except ValueError as e:
        messagebox.showerror("Ошибка ввода", str(e))



root = tk.Tk()
root.geometry('%dx%d+%d+%d' % (1585, 900, 150, 50))
root.title("Распределение предметов")


font = ('Arial', 16)


label_items = tk.Label(root, text="Количество предметов (T):", font=font)
label_items.pack(pady=5)
entry_items = tk.Entry(root, font=font, width=10)
entry_items.pack(pady=5)

label_people = tk.Label(root, text="Количество людей (K):", font=font)
label_people.pack(pady=5)
entry_people = tk.Entry(root, font=font, width=10)
entry_people.pack(pady=5)


label_max_items = tk.Label(root, text="Максимальное количество предметов для каждого человека:", font=font)
label_max_items.pack(pady=5)
entry_max_items = tk.Entry(root, font=font, width=10)
entry_max_items.pack(pady=5)


button_calculate = tk.Button(root, text="Рассчитать", command=calculate_distribution, font=font, width=15)
button_calculate.pack(pady=10)


output_text = scrolledtext.ScrolledText(root, width=40, height=10, font=font)
output_text.pack(pady=10)

root.mainloop()