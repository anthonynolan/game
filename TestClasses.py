#!/usr/bin/env python3

import unittest
from Room import Room

class TestClasses(unittest.TestCase):

    def setUp(self):
        self.room_name = 'A Big Room'
        self.room_desc = 'This is a nice big room'
        self.room = Room(self.room_name, self.room_desc)

    def test_str(self):
        # dummy str first to move the str to short form
        str(self.room)
        self.assertEqual(str(self.room), self.room_name)

    def test_repr(self):
        self.assertEqual(str(repr(self.room)), f'(name={self.room_name}, desc={self.room_desc}, items=[])')

    def test_add_take_item(self):
        an_item = 'Box Cutter'
        self.room.put(an_item)
        self.assertEqual(len(self.room), 1)
        taken = self.room.take(an_item)
        self.assertEqual(taken, an_item)
        self.assertEqual(len(self.room), 0)
        

if __name__=='__main__':
    unittest.main()
