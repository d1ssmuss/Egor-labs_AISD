"""
Задание на л.р. №7
Требуется для своего варианта второй части л.р. №6 (усложненной программы) разработать реализацию с использованием графического интерфейса.
Допускается использовать любую графическую библиотеку питона.
Рекомендуется использовать внутреннюю библиотеку питона  tkinter.
В программе должны быть реализованы минимум одно окно ввода, одно окно вывода (со скролингом), одно текстовое поле, одна кнопка.
"""
import time
import itertools
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

# Размеры животных (S - маленький, M - средний, L - большой)
animal_sizes = {
    "лев": "L",
    "тигр": "L",
    "волк": "M",
    "лиса": "M",
    "заяц": "S",
    "антилопа": "M",
    "попугай": "S",
    "змея": "S"
}

def count_size_violations(arrangement, size_to_avoid, dangerous_pairs):
    violations = 0
    for i in range(len(arrangement) - 1):
        if animal_sizes[arrangement[i]] == size_to_avoid and animal_sizes[arrangement[i + 1]] == size_to_avoid:
            violations += 1
        if (arrangement[i], arrangement[i + 1]) in dangerous_pairs or (arrangement[i + 1], arrangement[i]) in dangerous_pairs:
            violations += 1
    return violations

def find_best_size_arrangement(animals, size_to_avoid, dangerous_pairs):
    best_arrangement = None
    min_violations = float('inf')

    for perm in itertools.permutations(animals):
        violations = count_size_violations(perm, size_to_avoid, dangerous_pairs)
        if violations < min_violations:
            min_violations = violations
            best_arrangement = perm
            if min_violations == 0:  # идеальный вариант
                break

    return best_arrangement, min_violations

def on_calculate():
    try:
        selected_animals = [animal for animal, var in animal_vars.items() if var.get()]
        if len(selected_animals) > 8:
            messagebox.showerror("Ошибка", "Выбрано больше 8 животных. Выберите не более 8.")
            return
        elif len(selected_animals) == 0:
            messagebox.showerror("Ошибка", "Выберите хотя бы одно животное.")
            return

        size_to_avoid = size_var.get()
        if size_to_avoid not in ["S", "M", "L"]:
            messagebox.showerror("Ошибка", "Выберите размер (S, M или L).")
            return

        dangerous_pairs_input = entry_dangerous_pairs.get()
        dangerous_pairs = set()
        for pair in dangerous_pairs_input.split(','):
            animal1, animal2 = pair.strip().split()
            dangerous_pairs.add((animal1, animal2))

        start_time = time.time()
        best_arrangement, violations = find_best_size_arrangement(selected_animals, size_to_avoid, dangerous_pairs)
        end_time = time.time()

        output_text.delete(1.0, tk.END)
        if violations == 0:
            output_text.insert(tk.END, f"Оптимальная расстановка: {best_arrangement}\n")
        else:
            output_text.insert(tk.END, "Не найдено оптимальной расстановки!\n")
        output_text.insert(tk.END, f"Время выполнения: {end_time - start_time:.5f} секунд")

    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные данные!")

def on_size_select(size):
    size_var.set(size)

root = tk.Tk()
root.geometry('%dx%d+%d+%d' % (1500, 800, 200, 140))
root.title("Оптимальная расстановка животных")

# Стиль
style = ttk.Style()
style.configure("TLabel", font=("Arial", 14), padding=10)
style.configure("TButton", font=("Arial", 14), padding=10)
style.configure("TRadiobutton", font=("Arial", 14), padding=10)
style.configure("TCheckbutton", font=("Arial", 14), padding=10)

# Фрейм для выбора животных
animals_frame = ttk.Frame(root)
animals_frame.pack(pady=10)

# Поле для выбора животных
label_animals = ttk.Label(animals_frame, text="Выберите животных:")
label_animals.grid(row=0, column=0, columnspan=2, pady=5)

animal_vars = {}
row = 1
col = 0
for animal, size in animal_sizes.items():
    var = tk.BooleanVar()
    animal_vars[animal] = var
    checkbutton = ttk.Checkbutton(animals_frame, text=f"{animal} ({size})", variable=var)
    checkbutton.grid(row=row, column=col, sticky=tk.W, pady=2, padx=5)
    col = (col + 1) % 2
    if col == 0:
        row += 1

# Поле для выбора размера, который нужно избегать
size_var = tk.StringVar()
label_size = ttk.Label(root, text="Выберите размер, который нужно избегать:")
label_size.pack(anchor=tk.CENTER, pady=5)

size_frame = ttk.Frame(root)
size_frame.pack(pady=10)

for size in ["S", "M", "L"]:
    radiobutton = ttk.Radiobutton(size_frame, text=size, variable=size_var, value=size, command=lambda s=size: on_size_select(s))
    radiobutton.pack(side=tk.LEFT, padx=10)

# Ввод опасных пар
label_dangerous_pairs = ttk.Label(root, text="Введите опасные пары через запятую (например, волк заяц, лиса антилопа):")
label_dangerous_pairs.pack(anchor=tk.CENTER, pady=5)

entry_dangerous_pairs = ttk.Entry(root, width=50)
entry_dangerous_pairs.pack(pady=5)

calculate_button = ttk.Button(root, text="Рассчитать", command=on_calculate)
calculate_button.pack(pady=20)

# Вывод результата
output_frame = ttk.Frame(root)
output_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

output_text = scrolledtext.ScrolledText(output_frame, width=80, height=15, font=("Arial", 26))
output_text.pack(fill=tk.BOTH, expand=True)

root.mainloop()
