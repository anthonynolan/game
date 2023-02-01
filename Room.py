#!/usr/bin/env python3

import pdb

class Room:
    def __init__(self, name=None, desc='', items=[], dictionary=None):

        self.viewed = False
        self.puzzle = None
        self.desc = None

        if dictionary:
            for k, v in dictionary.items():
                setattr(self, k, v)
        else:
            self.name = name
            self.desc = desc
            self.items = items

    def __len__(self):
        return len(self.items)

    def take(self, item):
        removed = None
        try:
            self.items.remove(item)
            removed = item
        except:
            print(f'there was no {item} in the room')
        return removed

    def put(self, item):
        self.items.append(item)

    def __str__(self):
        if not self.viewed:
            self.viewed = True
            return f'{self.name}\n{self.desc}'
        return f'{self.name}'

    def __repr__(self):
        return f'(name={self.name}, desc={self.desc}, items={self.items})'
    
    