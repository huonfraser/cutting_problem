# =============================================================================
# Albert Bannister_1210510 Huon Fraser_1258237
# =============================================================================
from main import *
from placement import *
from random import randint
from neighbourhood import *
from view import *


file_m1a = "data/M1a.csv"
file_m2c = "data/M2c.csv"
file_m3d = "data/M3d.csv"

nh_short = neighbourhoods_short()
nh_med = neighbourhoods_med()
nh_long = neighbourhoods_long()

cut = cutting_problem(file_m1a,debug_mode=True,neighbourhood_functions=nh_short)

soln = cut.run()
cut.view()
