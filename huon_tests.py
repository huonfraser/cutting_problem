import skeleton

file = "data\M1a.csv"
data, width = skeleton.load(file)
lowerbound = data.area / width
upperbound = lowerbound * 4  # claculat upper bound

solution = skeleton.bottom_left_fill(data,width,upperbound)