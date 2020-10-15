# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 20:58:31 2020

@author: Ashish
"""

import random

def generate_random_geog_coords(qty):
    # Generate a set of all points within 200 of the origin, to be used as offsets later
    # There's probably a more efficient way to do this.
    radius = 200
    rangeX = (0, 2500)
    rangeY = (0, 2500)
    # qty = 100  # or however many points you want


    deltas = set()
    for x in range(-radius, radius+1):
        for y in range(-radius, radius+1):
            if x*x + y*y <= radius*radius:
                deltas.add((x,y))

    randPoints = []
    excluded = set()
    i = 0
    while i<qty:
        x = random.randrange(*rangeX)
        y = random.randrange(*rangeY)
        if (x,y) in excluded: continue
        randPoints.append((x,y))
        i += 1
        excluded.update((x+dx, y+dy) for (dx,dy) in deltas)
        # print (randPoints)
    return randPoints

# Implementation
geog_cords = generate_random_geog_coords(10)
print(geog_cords)