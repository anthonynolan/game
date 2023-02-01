#!/usr/bin/env python3

from utils import game_over, title

class Player:
    def __init__(self, name, inventory=[]):
        self.name = name
        self.inventory = inventory
        self.health = 15
    
    def fight(self, opponent_power):
        self.health-=opponent_power
        if self.health<=0:
            game_over('The last thing you see is the back of her stinking throat...\nYou were defeated in battle', self)
        else:
            title(f'you have survived. Your health is now {self.health}')

    def __str__(self):
        return f'{self.name} {self.inventory}'

    def __repr__(self):
        return f'(name={self.name}, inventory={self.inventory})'
    