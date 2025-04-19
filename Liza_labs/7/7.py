"""
Задание на л.р. №7
Требуется для своего варианта второй части л.р. №6 (усложненной программы) разработать реализацию с использованием графического интерфейса.
Допускается использовать любую графическую библиотеку питона.
Рекомендуется использовать внутреннюю библиотеку питона  tkinter.
В программе должны быть реализованы минимум одно окно ввода, одно окно вывода (со скролингом), одно текстовое поле, одна кнопка.
"""

import tkinter as tk
from tkinter import messagebox, scrolledtext
import itertools
import time

def generate_permutations_pythonic(animals):
    return list(itertools.permutations(animals))

def is_valid_permutation(permutation, constraints):
    for i in range(len(permutation) - 1):
        if (permutation[i], permutation[i+1]) in constraints or (permutation[i+1], permutation[i]) in constraints:
            return False
    return True

def count_dangerous_pairs(permutation, constraints):
    count = 0
    for i in range(len(permutation) - 1):
        if (permutation[i], permutation[i+1]) in constraints or (permutation[i+1], permutation[i]) in constraints:
            count += 1
    return count

def find_optimal_permutation(animals, constraints):
    permutations = generate_permutations_pythonic(animals)
    valid_permutations = [p for p in permutations if is_valid_permutation(p, constraints)]
    if valid_permutations:
        optimal_permutation = min(valid_permutations, key=lambda p: count_dangerous_pairs(p, constraints))
        return optimal_permutation
    else:
        return None

def on_add_constraint():
    animal1 = left_var.get()
    animal2 = right_var.get()
    if animal1 and animal2 and animal1 != animal2:
        constraints.add((animal1, animal2))
        constraints_text.insert(tk.END, f"{animal1} - {animal2}\n")
    else:
        messagebox.showwarning("Предупреждение", "Выберите два разных животных.")

def on_clear_constraints():
    constraints.clear()
    constraints_text.delete(1.0, tk.END)

def on_calculate():
    animals = [animal for animal, var in animal_vars.items() if var.get()]
    start_time = time.time()
    optimal_permutation = find_optimal_permutation(animals, constraints)
    end_time = time.time()

    if optimal_permutation:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Оптимальный вариант: {optimal_permutation}\nВремя выполнения: {end_time - start_time:.4f} секунд")
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Невозможно найти допустимую расстановку с заданными ограничениями.")



root = tk.Tk()
root.title("Оптимальная расстановка клеток в зоопарке")
root.geometry('%dx%d+%d+%d' % (1200, 800, 340, 120))

# Список животных
animals_list = ['Лев', 'Тигр', 'Медведь', 'Волк', 'Лиса', 'Заяц', 'Орёл', 'Сова', 'Крокодил', 'Питон']


animal_vars = {animal: tk.IntVar() for animal in animals_list}

# Переменные для выбора пар
left_var = tk.StringVar()
right_var = tk.StringVar()

# Мн-во для хранения ограничений
constraints = set()


selection_label = tk.Label(root, text="Выберите животных:", font=("Arial", 14, "bold"))
selection_label.pack(pady=10)


selection_frame = tk.Frame(root)
selection_frame.pack(padx=10, pady=10)

# Левый столбец
left_column_frame = tk.Frame(selection_frame)
left_column_frame.grid(row=0, column=0, padx=10)

# Правый столбец
right_column_frame = tk.Frame(selection_frame)
right_column_frame.grid(row=0, column=1, padx=10)

# Размещение чекбоксов в два столбца
for i, animal in enumerate(animals_list):
    if i < 5:
        checkbutton = tk.Checkbutton(left_column_frame, text=animal, variable=animal_vars[animal], font=("Arial", 12))
        checkbutton.grid(row=i, column=0, sticky='w')
    else:
        checkbutton = tk.Checkbutton(right_column_frame, text=animal, variable=animal_vars[animal], font=("Arial", 12))
        checkbutton.grid(row=i-5, column=0, sticky='w')

# Фрейм для выбора пар
pair_frame = tk.Frame(root)
pair_frame.pack(padx=10, pady=10)

left_label = tk.Label(pair_frame, text="Выберите первое животное:", font=("Arial", 12))
left_label.grid(row=0, column=0, padx=5)
left_dropdown = tk.OptionMenu(pair_frame, left_var, *animals_list)
left_dropdown.config(font=("Arial", 12))
left_dropdown.grid(row=1, column=0, padx=5)

right_label = tk.Label(pair_frame, text="Выберите второе животное:", font=("Arial", 12))
right_label.grid(row=0, column=1, padx=5)
right_dropdown = tk.OptionMenu(pair_frame, right_var, *animals_list)
right_dropdown.config(font=("Arial", 12))
right_dropdown.grid(row=1, column=1, padx=5)

add_button = tk.Button(pair_frame, text="Добавить ограничение", command=on_add_constraint, font=("Arial", 12))
add_button.grid(row=1, column=2, padx=5)

# Отображение ограничения
constraints_frame = tk.Frame(root)
constraints_frame.pack(padx=10, pady=10)

constraints_label = tk.Label(constraints_frame, text="Ограничения:", font=("Arial", 12))
constraints_label.pack()

constraints_text = scrolledtext.ScrolledText(constraints_frame, wrap=tk.WORD, width=80, height=5, font=("Arial", 12))
constraints_text.pack()

clear_button = tk.Button(constraints_frame, text="Очистить ограничения", command=on_clear_constraints, font=("Arial", 12))
clear_button.pack(pady=5)

# Кнопка расчёта
calculate_button = tk.Button(root, text="Рассчитать", command=on_calculate, font=("Arial", 12))
calculate_button.pack(pady=10)

# Поле вывода результата
result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=10, font=("Arial", 12))
result_text.pack(pady=10)

root.mainloop()
