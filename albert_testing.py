from skeleton import *
from placement import *
from random import randint
from view import *

file = "data\M1a.csv"
#cut = cutting_problem(file,debug_mode=False, reduced_descent = False,sort_criteria="none", rotate_criteria="none")
cut = cutting_problem(file,debug_mode=False)

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