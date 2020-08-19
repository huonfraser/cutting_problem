from skeleton import *
from placement import *
from random import randint
from view import *

file="data\\M1a.csv"
cut = cutting_problem(file, debug_mode=False, buffer=0.0, sort_criteria="height", rotate_criteria="up")
#cut = cutting_problem(file, debug_mode=False, buffer=0.0, sort_criteria="none", rotate_criteria="none")
solns = []

for i in range(0, 10):
    solution, final_height, avg_time, placements_searched = cut.run()
    solns.append(final_height)

print("Average " + str(sum(solns)/len(solns)))
print("Best " + str(min(solns)))

view(solution,cut.width,cut.upperbound)

#for s in ["area", "width", "height", "max", "min"]:
 #   print(s)
  #  cut = cutting_problem(file, debug_mode=False, buffer=0.0, sort_criteria=s,rotate_criteria="up")
   # soln = cut.run(num_iterations=0)
    #cut.view()

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