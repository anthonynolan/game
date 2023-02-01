#!/usr/bin/env python3

import pdb
from utils import show_status, title

class Puzzle:
    def __init__(self, q=None, a=None, points=None, dictionary=None):
        if dictionary:
            for k, v in dictionary.items():
                setattr(self, k, v)
        else:
            self.q = q
            self.a = a
            self.points = points
        self.asked = False

    def assign(self, player):
        self.player = player

    def __call__(self):
        if self.asked: 
            return
        print('We have a puzzle for. Answer correctly to win some health points.')
        answer = input(self.q)
        if answer==self.a:
            self.player.health+=int(self.points)
            show_status('congratulations', f'You have gained {self.points} health. Your new health is {self.player.health}')
        else:
            show_status('Wrong answer!', 'No extra health points for you.')
        self.asked=True