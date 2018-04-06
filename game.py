#!/usr/bin/python3
# coding: utf-8

import tkinter as tk


class Game(tk.Frame):

    def __init__(self, master):
        super(Game, self).__init__(master)
        self.lives = 3
        self.width = 610
        self.height = 400
        self.canvas = tk.Canvas(self, bg='#aaaaff', width=self.width, height=self.height)
        self.canvas.pack()
        self.pack()

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Hello, Pong !')
    game = Game(root)
    game.mainloop()

