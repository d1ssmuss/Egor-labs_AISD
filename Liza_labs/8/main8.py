"""
Задание на л.р. №8 ООП 24
Требуется написать ООП с графическим интерфейсом в соответствии со своим
вариантом.
Должны быть реализованы минимум один класс, три атрибута, четыре метода
(функции).
Ввод данных из файла с контролем правильности ввода.
Базы данных не использовать. При необходимости сохранять информацию в
файлах, разделяя значения запятыми (CSV файлы) или пробелами. Для GUI
использовать библиотеку tkinter (mathplotlib не использовать).

Вариант №12
Объекты – круги
Функции:
    - сегментация
    - визуализация
    - раскраска
    - зеркальное отображение относительно заданной оси
"""


import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import csv
import math

class Circle:
    def __init__(self, x, y, radius, color='red'):
        self.x = x  # центр x
        self.y = y  # центр y
        self.radius = radius
        self.color = color
        self.segments_count = 0  # количество сегментов

    def segment(self, canvas, segments=4):
        """
        Сегментация круга: рисуем хорды, делящие круг на 'segments' частей.
        """
        self.segments_count = segments
        angle_step = 2 * math.pi / segments

        coords = []
        for i in range(segments):
            angle = i * angle_step
            x_end = self.x + self.radius * tk.math.cos(angle)
            y_end = self.y + self.radius * tk.math.sin(angle)
            coords.append((x_end, y_end))

        # Рисуем линии от центра к точкам на окружности
        for (x_end, y_end) in coords:
            canvas.create_line(self.x, self.y, x_end, y_end, fill='gray', dash=(3, 3))

    def visualize(self, canvas):
        """
        Рисуем круг на указанном холсте tkinter.
        """
        x0 = self.x - self.radius
        y0 = self.y - self.radius
        x1 = self.x + self.radius
        y1 = self.y + self.radius
        canvas.create_oval(x0, y0, x1, y1, outline='black', width=2, fill=self.color)

    def colorize(self, color):
        """
        Изменение цвета круга.
        """
        self.color = color

    def mirror(self, axis='x'):
        """
        Зеркальное отображение круга относительно оси.
        axis: 'x' или 'y'.
        При отражении по оси X: y -> -y.
        При отражении по оси Y: x -> -x.
        """
        if axis == 'x':
            self.y = -self.y
        elif axis == 'y':
            self.x = -self.x


class CircleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Зеркальное отображение кругов")

        self.canvas_width = 800
        self.canvas_height = 600
        self.root.configure(bg='gray')

        self.root.geometry('%dx%d+%d+%d' % (1200, 800, 350, 150))

        self.circles = []  # список объектов Circle

        # Создаём элементы интерфейса
        self.create_widgets()

    def create_widgets(self):
        # Холст для рисования
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg='lightblue')
        self.canvas.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Кнопки
        button_frame = tk.Frame(self.root, bg='lightgray')
        button_frame.grid(row=1, column=0, columnspan=4, pady=10)

        self.load_btn = tk.Button(button_frame, text="Загрузить круги из файла", command=self.load_circles, bg='white', fg='black', font=15)
        self.load_btn.grid(row=0, column=0, padx=5, pady=5)

        self.segment_btn = tk.Button(button_frame, text="Сегментировать круги", command=self.segment_circles, bg='white', fg='black', font=15)
        self.segment_btn.grid(row=0, column=1, padx=5, pady=5)

        self.color_btn = tk.Button(button_frame, text="Раскрасить круги", command=self.colorize_circles, bg='white', fg='black', font=15)
        self.color_btn.grid(row=0, column=2, padx=5, pady=5)

        self.mirror_btn = tk.Button(button_frame, text="Отразить круги", command=self.mirror_circles, bg='white', fg='black', font=15)
        self.mirror_btn.grid(row=0, column=3, padx=5, pady=5)

        # Информационная метка
        self.info_label = tk.Label(self.root, text="Загрузите файл с данными кругов для начала работы.", bg='lightgray', fg='black', font=15)
        self.info_label.grid(row=2, column=0, columnspan=4, pady=5)

        # Центрируем все элементы
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def load_circles(self):
        # Диалог открытия файла
        file_path = filedialog.askopenfilename(
            title="Открыть файл с данными кругов",
            filetypes=[("Файлы CSV", "*.csv"), ("CSV файлы", "*.csv"), ("Все файлы", "*.*")]
        )
        if not file_path:
            return
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
            self.circles.clear()
            errors = []
            for idx, line in enumerate(lines, start=1):
                line = line.strip()
                if not line:
                    continue
                parts = line.replace(',', ' ').split()
                if len(parts) < 3:
                    errors.append(f"Строка {idx}: недостаточно данных")
                    continue
                try:
                    x = float(parts[0])
                    y = float(parts[1])
                    r = float(parts[2])
                    if r <= 0:
                        errors.append(f"Строка {idx}: радиус должен быть положительным")
                        continue
                    color = parts[3] if len(parts) > 3 else 'black'
                except ValueError:
                    errors.append(f"Строка {idx}: неверный формат данных")
                    continue

                circle = Circle(x, y, r, color)
                self.circles.append(circle)

            if errors:
                messagebox.showwarning("Предупреждения при загрузке", "\n".join(errors))

            self.info_label.config(text=f"Загружено {len(self.circles)} кругов из файла.")
            self.redraw_canvas()
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить файл:\n{e}")

    def redraw_canvas(self):
        self.canvas.delete("all") # очищаем доску
        # Рисуем оси координат для ориентира
        self.canvas.create_line(self.canvas_width//2, 0, self.canvas_width//2, self.canvas_height, fill='blue', dash=(50, 1))
        self.canvas.create_line(0, self.canvas_height//2, self.canvas_width, self.canvas_height//2, fill='blue', dash=(50, 1))

        # Переводим координаты круга в координаты холста (центр холста по центру)
        for circle in self.circles:
            cx = circle.x + self.canvas_width//2
            cy = self.canvas_height//2 - circle.y  # координата y инвертирована для холста
            x0 = cx - circle.radius
            y0 = cy - circle.radius
            x1 = cx + circle.radius
            y1 = cy + circle.radius
            try:
                self.canvas.create_oval(x0, y0, x1, y1, outline='black', width=2, fill=circle.color)
            except tk.TclError:
                # Если цвет некорректен, показываем предупреждение, но не меняем круги и не очищаем
                messagebox.showerror("Ошибка цвета", f"Некорректный цвет: {circle.color}. Круг не будет перекрашен.")
                # Можно временно задать фигурке цвет по умолчанию или пропустить рисование вовсе
                self.canvas.create_oval(x0, y0, x1, y1, outline='black', width=2, fill='gray')

            # Если есть сегменты, рисуем линии сегментации
            if circle.segments_count > 0:
                self.draw_segments(circle, cx, cy)

    def draw_segments(self, circle, cx, cy):
        segments = circle.segments_count
        angle_step = 2 * math.pi / segments
        for i in range(segments):
            angle = i * angle_step
            x_end = cx + circle.radius * math.cos(angle)
            y_end = cy + circle.radius * math.sin(angle)
            self.canvas.create_line(cx, cy, x_end, y_end, fill='black', dash=(2, 10))

    def segment_circles(self):
        if not self.circles:
            messagebox.showinfo("Информация", "Круги не загружены для сегментации.")
            return
        segments = simpledialog.askinteger("Ввод", "Введите количество сегментов для каждого круга:", minvalue=1, maxvalue=20, initialvalue=4)
        if segments is None:
            return
        for circle in self.circles:
            circle.segments_count = segments
        self.redraw_canvas()

    def colorize_circles(self):
        if not self.circles:
            messagebox.showinfo("Информация", "Круги не загружены для раскраски.")
            return
        color = simpledialog.askstring("Ввод", "Введите название цвета или HEX-код (например red или #ff0000):")
        if not color:
            return

        # Попробуем применить цвет к одному временно для проверки
        # Если цвет неверный, tkinter выдаст исключение при fill
        try:
            # Проверим, применим цвет к временной фигуре на холсте
            temp_id = self.canvas.create_oval(0, 0, 1, 1, fill=color)
            self.canvas.delete(temp_id)
        except tk.TclError:
            messagebox.showerror("Ошибка цвета", f"Введён некорректный цвет: {color}. Попробуйте снова.")
            return

        # Если цвет OK, применяем ко всем кругам
        for circle in self.circles:
            circle.colorize(color)
        self.redraw_canvas()

    def mirror_circles(self):
        if not self.circles:
            messagebox.showinfo("Информация", "Круги не загружены для зеркального отображения.")
            return
        axis = simpledialog.askstring("Ввод", "Введите ось для зеркального отображения (x или y):")
        if axis not in ('x', 'y'):
            messagebox.showerror("Ошибка", "Некорректная ось. Введите 'x' или 'y'.")
            return
        for circle in self.circles:
            circle.mirror(axis)
        self.redraw_canvas()


if __name__ == "__main__":
    root = tk.Tk()
    app = CircleApp(root)
    root.mainloop()
