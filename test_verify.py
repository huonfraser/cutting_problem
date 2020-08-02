from skeleton import *

sol1 = Solution([
    ("a",0,0,4,4),
    ("b",5,5,4,4)

])

#correct

sol2 = Solution([
    ("a",0,0,4,4),
    ("b",0,0,4,4)

])
#correct

sol3 = Solution([
    ("a",0,0,4,4),
    ("b",1,1,2,2)

])
#correct

sol4 = Solution([
    ("a",0,0,4,4),
    ("b",3,3,5,5)

])
#correct

sol5 = Solution([
    ("a",0,0,4,4),
    ("b",0,5,5,5)

])
#correct
sol6 = Solution([
    ("a",0,0,4,4),
    ("b",5,0,5,5)

])
#correct

sol7 = Solution(
    [
        ("a",0,0,2,2),
        ("b",2,2,2,2)
    ]
)

print(sol7.verify())