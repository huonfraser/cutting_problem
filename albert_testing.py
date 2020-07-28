# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 15:07:35 2020

@author: albib
"""


from skeleton import *
from random import randint

def placeZero(data):
    rectangles = data.data
    placed_rectangles = []
    for rect in rectangles:
        id = rect[0]
        width = rect[1]
        height = rect[2]
        placed_rectangles.append((id,0,0,width,height))
    
    return Solution(placed_rectangles)


data,width = load("data\M1a.csv")

# =============================================================================
# stuff = []
# for i in range(0,5):
#     stuff.append(i)
# 
# neighbourhood = neighbourhood_insert(stuff)
# print(neighbourhood)
# =============================================================================

random_solution = place_random(data, 800, 400)
print(random_solution)
view(random_solution, 800, 400)

#Step 2: Generate initial soln
#solution = place_random(data,800,400)
#view(solution)
#print(solution.soln)
