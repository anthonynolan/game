#!/usr/bin/env python3

from Puzzle import Puzzle
from room_builder import load_rooms
from utils import title, show_list, show_status
from collections import deque
from Player import Player
import numpy as np
import pdb
from datetime import datetime

class Game:

    def __init__(self, player):
        self.rooms = load_rooms()

        class History:
            def __init__(self):
                self.history = list()
            def add_entry(self, room):
                self.history.append((datetime.now().isoformat(), room.name))
            def __iter__(self):
                return iter(self.history)
            def show(self):
                show_list("History", iter(self))

        self.history = History()
        self.inventory = []
        self.location = 1
        self.player=player
        self.current_room = self.rooms[self.location]
        self.monster_location = len(self.rooms) - 1

        show_list("Rooms", [r.name for r in self.rooms])

    def check_instructions(self, inst):
        words = inst.split()
        if words[0] == "go":
            return {"command": "go", "details": words[1]}
        elif words[0] == "get":
            return {"command": "get", "details": words[1]}
        else:
            return {"command": words[0]}


    def print_location(self):

        show_status("You are in", self.current_room)

        if len(self.current_room):
            show_status("On the floor", self.current_room.items)

        show_status("Inventory", self.inventory)

        if self.monster_location == self.location:
            if "sword" in self.inventory:
                self.monster_location = -1
                title("you have killed the monster!!!")
            elif "armour" not in self.inventory:
                title("There is a huge monster here. You are going to fight her.")
                self.player.fight(10)
            else:
                title("The monster attacked you, but your armour saved you this time!")
                self.player.inventory.remove("armour")


    

    def move_monster(self):
        if self.monster_location != -1:
            if np.random.randn() > 0.5:
                if self.monster_location == len(self.rooms) - 1:
                    self.monster_location = 0
                else:
                    self.monster_location += 1
            else:
                if self.monster_location == 0:
                    self.monster_location = len(self.rooms) - 1
                else:
                    self.monster_location -= 1

        show_status("The monster is in",self.rooms[self.monster_location])


    def read_instructions(self):
        self.print_location()

        inst = input("What would you like to do?")

        result = self.check_instructions(inst)
        if result["command"] == "history":
            self.history.show()
        elif result["command"] == "go":
            self.go(result['details'])
            self.move_monster()
        elif result["command"] == "get":
            self.inventory.append(self.current_room.take(result['details']))

    def go(self, direction):
        if direction == "north":
            if self.location == len(self.rooms) - 1:
                self.location = 0
            else:
                self.location += 1

        elif direction=='south':
            if self.location == 0:
                self.location = len(self.rooms) - 1
            else:
                self.location -= 1

        self.current_room = self.rooms[self.location]
        self.history.add_entry(self.current_room)

        pdb.set_trace()
        if self.current_room.puzzle:
            p = Puzzle(dictionary=self.current_room.puzzle)
            p.assign(self.player)
            p()


    def start(self):
        while True:
            self.read_instructions()

if __name__ == "__main__":
    name = input("What is your name? (hit return for Cathal)")
    if len(name)<=0:
        name = "Cathal"
    player = Player(name)
    game = Game(player=player)
    game.start()
    
