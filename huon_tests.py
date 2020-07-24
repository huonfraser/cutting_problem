import skeleton

file = "data\M1a.csv"
data, width = skeleton.load(file)
lowerbound = data.area / width
upperbound = lowerbound * 4  # claculat upper bound

#solution = skeleton.bottom_left_fill(data,width,upperbound)

rect1 = (1,100,100,10,10)
rect2 = (2,10,0,40,20)

rects = skeleton.Solution([rect1])

skeleton.view(rects)