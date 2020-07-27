import Polygon #library for handling polygons https://pypi.org/project/Polygon/#:~:text=Polygon%20is%20a%20python%20package,in%20a%20very%20intuitive%20way.
import Polygon.Shapes
from random import randint
import skeleton

def place_random(data, window_height, window_width):
    rectangles = data.data
    placed_rectangles = []
    for rect in rectangles:
        x_pos = randint(0 ,window_width)
        y_pos = randint(0 ,window_height)
        id = rect[0]
        width = rect[1]
        height = rect[2]
        placed_rectangles.append((id ,x_pos ,y_pos ,width ,height))

    return skeleton.Solution(placed_rectangles)

def no_fill_polygon(poly1, poly2):
    """
    Return nfp of polygon 1 and polygon2, places around polygon 1 that polygon 2 can be placed
    :param poly1: the free space polygon
    :param poly2: the polygon to be filled
    :return: position of the bottom left corner of the polygon
    """


    # search free free area for points
    # try bottom most left one where fits, nfp polygon

    # return x,y
    tristrip = poly1.triStrip()
    triangles = tristrip_to_triangles(tristrip)
    # order triangles by smallest x, smallest y if equal
    for t in triangles:
        # try to fit in bottom left
        # if fit,poly2 inside poly1 ,return
        pass
        # else continue

    # should never reach this point


    pass

def tristrip_to_triangles(tristrip):
    tristrip = tristrip[0]
    triangles = []
    for i in range(0 ,len(tristrip ) -2):
        val1 = (tristrip[i])
        val2 = (tristrip[ i +1])
        val3 = (tristrip[ i +2])
        # find bottom left triangle, order bottomleft,bottomright,top (do we ignore top right triangle)
        triangles.append((val1 ,val2 ,val3))

    # print(triangles)
    return triangles

def _create_rectangle(x ,y ,width ,height):
    return Polygon.Polygon([(x ,y) ,( x +width ,y) ,( x +width , y +height) ,(x , y +height) ,(x ,y)])

def bottom_left_fill(data, width,upperbound):
    #place each item in data, in order

    #generate a union polygon of placed, of size less than width
    #we can take disjoint set of this and width, and edges of this to generate NFP
    #we will need a no-fill-polygon for placement points

    free_area = Polygon.Shapes.Rectangle(width,upperbound) #set roll
    solns = []
    print(free_area)

    for i in data.data:

        i_id = i[0]
        i_w = i[1]
        i_h = i[2]

        poly_rep = Polygon.Shapes.Rectangle(i_w, i_h) #polygon representation of this shape, floating in space
        x, y = no_fill_polygon(free_area,poly_rep) #calculate position of polygon
        solns.append(i_id,x,y,i_w,i_h) # add soln

        free_area = free_area - _create_rectangle(x,y,i_w,i_h) #calculate new free area

    return solns