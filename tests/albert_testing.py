from main import *
from placement import *
from random import randint
from neighbourhood import *
from view import *




file_m1a = "../data/M1a.csv"
file_m2c = "../data/M2c.csv"
file_m3d = "../data/M3d.csv"


nh_2_desc = neighbourhoods_2_desc()
nh_2_cycle = neighbourhoods_2_cycle()
nh_3_desc = neighbourhoods_3_desc()
nh_3_cycle = neighbourhoods_3_cycle()
nh_1 = neighbourhoods_1()
nh_block1 = [nh_block1]
nh_test = nh_test1()


#nh_small_insert = nh_small.append(nh_insert)

#cut = cutting_problem(file,debug_mode=False, reduced_descent = False,sort_criteria="none", rotate_criteria="none")
#m3d = cutting_problem(file,debug_mode=False, neighbourhood_functions = neighbourhoods)
cut = cutting_problem(file_m2c,debug_mode=False,neighbourhood_functions=nh_test)

# =============================================================================
# experiments = []
# 
# experiments.append(cutting_problem(file_m1a,debug_mode=False,neighbourhood_functions=nh_small))
# experiments.append(cutting_problem(file_m2c,debug_mode = False,neighbourhood_functions=nh_small))
# experiments.append(cutting_problem(file_m3d,debug_mode=False,neighbourhood_functions=nh_small))
# =============================================================================

# =============================================================================
# results = []
# for exp in experiments:
#     solution, final_height, avg_time, placements_searched = exp.run()
#     results.append(final_height)
#     print(str(solution))
#     view(solution,exp.width,exp.upperbound)
# =============================================================================
#soln = cut.run(num_iterations=5)
#soln = cut.initial_solution(sort_criteria="none", rotate_criteria="none")
soln = cut.run()
cut.view()
#data, width = load(file)
#random_solution = place_random(data,800,400)

#lowerbound = data.area / width
#upperbound = lowerbound * 4  # claculat upper bound




#rects = bottom_left_fill(data, width, upperbound)
#print(rects.soln)


#solution = skeleton.bottom_left_fill(data,width,upperbound)

#rect1 = (1,0.0,0.0,2.0,6.0)
#rect2 = (2,10.0,0.0,6.0,2.0)

#rects = Solution([rect1])

#view(random_solution)
#view(rects,width,upperbound)