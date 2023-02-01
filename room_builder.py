#!/usr/bin/env python3

import json
from Room import Room
from Puzzle import Puzzle
from utils import title, MyEncoder
import pdb
import jsonpickle

FILE_LOCATION = "new_rooms.json"


def load_rooms():
    rooms = []

    with open(FILE_LOCATION, "rt") as f:
        js = f.read()
        rooms = jsonpickle.decode(js)
    

    # for room in json_rooms:
    #     temp_room = Room(dictionary=room)
    #     temp_room.viewed = False
    #     rooms.append(temp_room)

    return rooms

def read_write():
    rooms = load_rooms()
    pdb.set_trace()
    save_rooms(rooms)



def save_rooms(rooms):
    # rooms = {
    #     0: {"name": "The dungeon", "items": ["chain"]},
    #     1: {"name": "The castle", "items": ["armour"]},
    #     2: {"name": "shit biscuits", "items": ["gold"]},
    #     3: {"name": "Dog Central", "items": ["bruno"]},
    #     4: {"name": "The secret tunnel room", "items": []},
    # }

    with open(FILE_LOCATION, "wt") as f:
        js = jsonpickle.encode(rooms)
        f.write(js)
    print("rooms saved")


def create_room():
    rooms = load_rooms()
    print("create room")
    name = input("What is the name of the room? ")
    items = input("What is in the room (comma separate items)?")
    rooms.append(dict(name=name, items=items.split(",")))
    save_rooms(rooms)

def create_puzzle():
    rooms = load_rooms()
    for i, room in enumerate(rooms):
        print(i, room)

    title('Create Puzzle')
    room = int(input('Enter room number?'))
    question = input('Question? ')
    answer = input('Answer?')
    points = input('Points for correct answer?')
    p = Puzzle(question, answer, points)
    rooms[room].puzzle = p
    save_rooms(rooms)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        if sys.argv[1] == "load":
            rooms = load_rooms()
            print(rooms)
        elif sys.argv[1] == "save":
            save_rooms(None)
        elif sys.argv[1] == "create_room":
            create_room()
        elif sys.argv[1] == "create_puzzle":
            create_puzzle()
        elif sys.argv[1]=='read_write':
            read_write()
    else:
        print("Enter a command, load, save, create_room, create_puzzle, read_write")
