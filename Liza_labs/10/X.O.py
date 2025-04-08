from tkinter import *
from tkinter.messagebox import showinfo


class TicTacToe:

    def __init__(self, master):
        self.master = master
        self.master.title('Крестики-нолики')
        self.master.geometry('%dx%d+%d+%d' % (700, 700, 600, 150))
        self.master.config(bg="#0080FF")
        self.game_title = Label(master, text="TicTacToe", font=("Times New Roman", 50), background="#0080FF",
                                foreground="#FFFFFF")
        self.game_title.pack(pady=50)

        self.play_ai = Button(master, text="Против Компьютера", font=("Arial", 25), command=self.start_game,
                              activebackground="#00868B", bd=3, bg="#0080FF", padx=10, pady=5, width=20, fg="#FFFFFF")

        self.exit = Button(master, text="Выйти из игры", font=("Arial", 25), command=master.destroy,
                           activebackground="#00868B", anchor="center", bd=3, bg="#0080FF", padx=10, pady=5, width=15,
                           fg="#FFFFFF")

        self.play_ai.pack(pady=20)
        self.exit.pack(pady=20)

        self.current_player = "X"
        self.maps = [""] * 9

    def start_game(self):
        self.hide_menu()
        self.create_game_board()

    def hide_menu(self):
        self.game_title.pack_forget()
        self.play_ai.pack_forget()
        self.exit.pack_forget()

    def create_game_board(self):
        self.board_frame = Frame(self.master)
        self.board_frame.pack(pady=20)

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = Button(self.board_frame, text="", font=("Arial", 20), width=5, height=2,
                                            command=lambda x=i, y=j: self.make_move(x, y))
                self.buttons[i][j].grid(row=i, column=j)

        self.back_button = Button(self.master, text="Назад", font=("Arial", 20), command=self.back_to_menu,
                                  bg="#0080FF", activebackground="#00868B")
        self.back_button.pack(pady=10)

    def back_to_menu(self):
        self.board_frame.pack_forget()
        self.back_button.pack_forget()
        self.show_menu()

    def show_menu(self):
        self.game_title.pack(pady=50)
        self.play_ai.pack(pady=20)
        self.exit.pack(pady=20)

    def make_move(self, x, y):
        if self.buttons[x][y]['text'] == "":
            self.buttons[x][y]['text'] = self.current_player
            self.buttons[x][y]['fg'] = "Blue" if self.current_player == "X" else "Red"
            self.maps[x * 3 + y] = self.current_player

            if self.check_winner(self.current_player):
                showinfo("Победа", "Игрок О победил!")
                self.reset_game()
            elif self.is_draw():
                showinfo("Ничья", "Игра закончилась вничью!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.AI()

    def check_winner(self, player):
        for row in range(3):
            if all(self.buttons[row][col]['text'] == player for col in range(3)):
                return True
        for col in range(3):
            if all(self.buttons[row][col]['text'] == player for row in range(3)):
                return True
        if all(self.buttons[i][i]['text'] == player for i in range(3)):
            return True
        if all(self.buttons[i][2 - i]['text'] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        return all(self.buttons[i][j]['text'] != "" for i in range(3) for j in range(3))

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ""
                self.maps[i * 3 + j] = ""
        self.current_player = "X"

    def check_line(self, sum_O, sum_X):
        step = ""
        victories = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for line in victories:
            o = sum(1 for j in line if self.maps[j] == "O")
            x = sum(1 for j in line if self.maps[j] == "X")

            if o == sum_O and x == sum_X:
                for j in line:
                    if self.maps[j] != "O" and self.maps[j] != "X":
                        step = j
        return step

    def AI(self):
        step = ""
        step = self.check_line(2, 0)
        if step == "":
            step = self.check_line(0, 2)
        if step == "":
            step = self.check_line(1, 0)
        if step == "":
            if self.maps[4] == "":
                step = 4
        if step == "":
            for i in range(9):
                if self.maps[i] == "":
                    step = i
                    break
        if step != "":
            x, y = divmod(step, 3)
            self.make_move(x, y)


if __name__ == "__main__":
    root = Tk()
    app = TicTacToe(root)
    root.mainloop()
