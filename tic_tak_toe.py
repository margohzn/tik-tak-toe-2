from tkinter import * 
import random
from tkinter import messagebox


class Tik_tak_toe:

    def __init__(self, window2, mode):
        self.window = window2
        self.mode = mode
        self.current_player = "X"
        self.score = {"X":0, "O":0} #this is the dictionary with the key first and then the score
        self.buttons = [[None for i in range(3)]for i in range(3)]
        self.creat_widgets()

    def creat_widgets(self):
        self.score_label = Label(self.window, text = self.get_score(), font = ("times", 20))
        self.score_label.grid(row = 0, column = 0, columnspan = 3, pady = 10)
        for row in range(3):
            for column in range(3):
                button_widget = Button(self.window, text = "", font = ("times", 40), width = 5, height = 2, command = lambda r = row, c = column: self.on_button_click(r,c)) #you use lambda when you need to pass information into the fonction
                button_widget.grid(row = row+1, column = column)
                self.buttons[row][column] = button_widget


class Menu:
    
    def __init__(self, window1):
        self.window = window1
        self.window.title("Tic Tak Toe starting page")
        self.create_widjts()
        
    def create_widjts(self):
        title = Label(self.window, text = "Select Mode", font = ("normal", 20)).pack(pady = 15, padx = 15)
        button1 = Button(self.window, text = "Single Player", font = ("times", 15), command = self.start_single_player).pack(pady = 15, padx = 15)
        button2 = Button(self.window, text = "Multi Player", font = ("times", 15), command = self.start_multi_player).pack(pady = 15, padx = 15)

    def start_single_player(self):
        self.window.destroy()
        self.start_game("single")

    def start_multi_player(self):
        self.window.destry()
        self.start_game("multi")

    def start_game(self, mode):
        window2 = Tk()
        Tik_tak_toe(window2, mode)
        window2.mainloop()


if __name__ == "__main__":
    window1 = Tk()
    Menu(window1)


window1.mainloop()
