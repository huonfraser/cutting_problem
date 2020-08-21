from skeleton import *
from placement import *
from random import randint
from neighbourhood import *
from view import *




file_m1a = "data\m1a.csv"
file_m2c = "data\m2c.csv"
file_m3d = "data\m3d.csv"

nh_short = neighbourhoods_short()
nh_med = neighbourhoods_med()
nh_long = neighbourhoods_long()

cut = cutting_problem(file_m1a,debug_mode=False,neighbourhood_functions=nh_med,rotate_criteria="up",sort_criteria="height")


soln = cut.run()
cut.view()
