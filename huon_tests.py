from skeleton import *

file = "data\M1a.csv"
data, width = load(file)
random_solution = place_random(data,800,400)

lowerbound = data.area / width
upperbound = lowerbound * 4  # claculat upper bound

rects = bottom_left_fill(data,width,upperbound)

#solution = skeleton.bottom_left_fill(data,width,upperbound)

#rect1 = (1,400.0,300.0,2.0,6.0)
#rect2 = (2,10.0,0.0,6.0,2.0)

#rects = Solution([rect1,rect2])

#view(random_solution)
view(rects)