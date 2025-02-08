from tkinter import *
import random
import tkinter.messagebox
from PIL import Image, ImageTk

class App:
    def __init__(self, master):
        self.master = master
        self.correct_word = random.choice(open("Egor_Wordle\Words(wordle).txt", "r", encoding='utf-8').read().split())
        self.correct_word = self.correct_word.upper()
        print("Подсказка(используется для тестирования): " + self.correct_word)
        self.master.title("Вордли (аналог популярной игры) v 1.0")
        self.master.geometry('%dx%d+%d+%d' % (1175, 1060, 350, 0))

        self.label = Label(text="Wordle", font=("Tahoma", 35))
        self.label.pack(anchor='n')

        self.alphabet = ["ЙЦУКЕНГШЩЗХЪ", "ФЫВАПРОЛДЖЭ", "ЯЧСМИТЬБЮ"]
        self.create_keyboard()
        self.create_game_board()
        self.current_row = 0
        self.current_col = 0
        self.current_guess = [""] * 5

    def create_game_board(self):
        self.game_board = Frame(self.master)
        self.game_board.pack(pady=20)

        self.guesses = []
        for i in range(6):  # 6 попыток
            row = []
            for j in range(5):  # 5 букв в слове
                cell = Label(self.game_board, text="", width=4, height=2, font=("Tahoma", 24), bg="white", relief="solid")
                cell.grid(row=i, column=j, padx=5, pady=5)
                row.append(cell)
            self.guesses.append(row)

    def create_keyboard(self):
        self.keyboard = Frame(self.master)
        self.keyboard.pack(pady=20)

        self.buttons = {}
        for row_idx, row in enumerate(self.alphabet):
            for col_idx, char in enumerate(row):
                button = Button(self.keyboard, text=char, width=4, height=2, font=("Tahoma", 18),
                               command=lambda c=char: self.on_key_press(c))
                button.grid(row=row_idx, column=col_idx, padx=5, pady=5)
                self.buttons[char] = button

        backspace_button = Button(self.keyboard, text="←", width=4, height=2, font=("Tahoma", 18),
                                  command=self.on_backspace)
        backspace_button.grid(row=0, column=len(self.alphabet[0]) + 1, padx=5, pady=5)

        enter_button = Button(self.keyboard, text="Enter", width=8, height=2, font=("Tahoma", 18),
                              command=self.on_enter)
        enter_button.grid(row=1, column=len(self.alphabet[1]) + 1, padx=5, pady=5, columnspan=2)

        help_button = Button(self.keyboard, text="Help", width=8, height=2, font=("Tahoma", 18),
                              command=self.on_help)
        help_button.grid(row=2, column=len(self.alphabet[1]) + 1, padx=5, pady=5, columnspan=2)

    def on_key_press(self, char):
        if self.current_col < 5:
            self.current_guess[self.current_col] = char
            self.guesses[self.current_row][self.current_col].config(text=char)
            self.current_col += 1

    def on_backspace(self):
        if self.current_col > 0:
            self.current_col -= 1
            self.current_guess[self.current_col] = ""
            self.guesses[self.current_row][self.current_col].config(text="")

    def on_help(self):
        self.help_window = Toplevel(self.master)
        self.help_window.title("Как играть?")
        self.help_window.geometry("800x800")

        # Загрузка изображения с помощью Pillow
        image_help = Image.open("Egor_Wordle/help_wordle.png")
        image_help = ImageTk.PhotoImage(image_help)

        # Отображение изображения в Label
        my_label = Label(self.help_window, image=image_help)
        my_label.image = image_help  # Сохраняем ссылку на изображение, чтобы оно не было удалено сборщиком мусора
        my_label.pack()

    def on_enter(self):
        if self.current_col == 5:
            guess_word = ''.join(self.current_guess)
            if guess_word == self.correct_word:
                self.check_guess(guess_word)
                tkinter.messagebox.showinfo("Победа!", "Вы угадали слово!")
                self.reset_game()
            else:
                self.check_guess(guess_word)
                self.current_row += 1
                self.current_col = 0
                self.current_guess = [""] * 5
                if self.current_row == 6:
                    tkinter.messagebox.showinfo("Проигрыш", f"Вы не угадали слово. Правильное слово: {self.correct_word}")
                    self.reset_game()
        else:
            tkinter.messagebox.showinfo("Длина слова меньше 5 букв!", "Слово должно состоять из 5 букв!")


    def check_guess(self, guess_word):
        correct_word_list = list(self.correct_word)
        guess_word_list = list(guess_word)
        correct_positions = [False] * 5

        # Первый проход: проверка точных совпадений
        for i in range(5):
            if guess_word_list[i] == correct_word_list[i]:
                self.guesses[self.current_row][i].config(bg="green")
                self.buttons[guess_word_list[i]].config(bg="green")
                correct_positions[i] = True
                correct_word_list[i] = None  # Отмечаем букву как использованную

        # Второй проход: проверка наличия букв в слове
        for i in range(5):
            if not correct_positions[i] and guess_word_list[i] in correct_word_list:
                self.guesses[self.current_row][i].config(bg="yellow")
                if self.buttons[guess_word_list[i]]['bg'] != "green":
                    self.buttons[guess_word_list[i]].config(bg="yellow")
                correct_word_list[correct_word_list.index(guess_word_list[i])] = None  # Отмечаем букву как использованную
            elif not correct_positions[i]:
                self.guesses[self.current_row][i].config(bg="gray")
                if self.buttons[guess_word_list[i]]['bg'] not in ["green", "yellow"]:
                    self.buttons[guess_word_list[i]].config(bg="gray")

    def reset_game(self):
        self.correct_word = random.choice(open("Egor_Wordle\Words(wordle).txt", "r", encoding='utf-8').read().split())
        self.correct_word = self.correct_word.upper()
        print(f"(Перезапуск игры) правильное слово: {self.correct_word}")
        for row in self.guesses:
            for cell in row:
                cell.config(text="", bg="white")
        for button in self.buttons.values():
            button.config(bg="SystemButtonFace")
        self.current_row = 0
        self.current_col = 0
        self.current_guess = [""] * 5

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
