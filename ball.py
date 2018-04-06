#! usr/bin/python3.5
# coding : utf-8

from game_object import GameObject

class Ball(GameObject):
    def __init__(self, canvas, x, y):
        self.radius = 10
        self.direction = [1, -1]
        self.speed = 10
        item = canvas.create_oval(x-self.radius, y-self.radius, x+self.radius, y+self.radius, fill="white")
        super(Ball, self).__init__(canvas, item)