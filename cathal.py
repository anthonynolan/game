#!/usr/bin/env python3


import math

while True:
    shape = input("what shape? ")
    if shape == "circle":
        print("area of circle")
        diameter = input("What is the diameter? ")
        area = math.pi * (float(diameter) / 2**2)
        print(f"The area is {area}")
    elif shape == "triangle":
        base = input("what is the base?")
        height = input("what is the height")
        print(f"Area is {float(base)*float(height)/2}")
    else:
        break
