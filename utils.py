#!/usr/bin/env python3

import sys
import json
from pyfiglet import Figlet

def title(text):
        f = Figlet()
        print(f.renderText(text))

def star_title(text):
        col_width = 80
        stars = (col_width - len(text)) // 2
        for index in range(0, len(text), col_width):
                print("".join(["*"] * stars) + text[index:index+50] + "".join(["*"] * stars))

def show_list(title_text, items):
        title(title_text)
        for item in items:
                print(f'* {item}')
        print()

def show_status(title_text, details):
        print(f'{title_text.title()}: \n')
        if isinstance(details, list):
                for item in details:
                        print(f'* {item}')
        else:
                print(details)
        print()

def game_over(reason, player):
        title(f'game over {player.name}')
        title(reason)
        title('')
        sys.exit()


class MyEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__