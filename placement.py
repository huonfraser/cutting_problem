import Polygon #library for handling polygons https://pypi.org/project/Polygon/#:~:text=Polygon%20is%20a%20python%20package,in%20a%20very%20intuitive%20way.
import Polygon.Shapes
import Polygon.IO
from random import randint
import skeleton
import view

def place_random(data, window_width, window_height):
    rectangles = data.data
    placed_rectangles = []

    for rect in rectangles:
        width = rect[1]
        height = rect[2]
        x_pos = randint(0, window_width-width)
        y_pos = randint(0, window_height-height)
        id = rect[0]

        placed_rectangles.append((id ,x_pos ,y_pos ,width ,height))

    return skeleton.Solution(placed_rectangles)

def order_triangles(tri1):
    #triangle of format ((x1,y1),(x2,y2),(x3,y3)), where x1,y1 bottom left
    bottom_left = tri1[1]
    pre = int(bottom_left[1])
    suf = int(bottom_left[0])
    full = str(pre)+"."+str(suf) #sort by y first then by x if y equal
    return(float(full))



def no_fill_polygon(area,poly1, poly2):
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
    triangles.sort(key=order_triangles)     # order triangles by smallest x, smallest y if equal
    #print(triangles)

    filled_area = area-poly1

    for t in triangles:
        x,y = t[0]
        poly2.shift(x,y)
        #print(poly2)
        #if(poly1.covers(poly2)):
        if not poly2.overlaps(filled_area):
            print("can place at",x,y)
            return x,y
        else:
            print("clash")

        # else continue

    # should never reach this point


    pass

def tristrip_to_triangles(tristrip):

    triangles = []
    for tri in tristrip:
        for i in range(0,len(tri) -2):
            val1 = (tri[i])
            val2 = (tri[ i +1])
            val3 = (tri[ i +2])
            # find bottom left triangle, order bottomleft,bottomright,top (do we ignore top right triangle)

            minx = min(min(val1[0],val2[0]),val3[0])
            miny = min(min(val1[1], val2[1]), val3[1])
            #print(minx,miny)
            if val1 == (minx,miny) or val2 == (minx,miny) or val3 == (minx,miny): #ignore topright
                triangles.append((val1 ,val2 ,val3))

    # print(triangles)
    #view.view_triangle(triangles)

    return triangles

def _create_rectangle(x ,y ,width ,height):
    return Polygon.Polygon([(x ,y) ,( x +width ,y) ,( x +width , y +height) ,(x , y +height) ,(x ,y)])

def bottom_left_fill(data, width,upperbound):
    #place each item in data, in order

    #generate a union polygon of placed, of size less than width
    #we can take disjoint set of this and width, and edges of this to generate NFP
    #we will need a no-fill-polygon for placement points

    free_area = Polygon.Shapes.Rectangle(width,upperbound) #set roll
    total_area = Polygon.Shapes.Rectangle(width,upperbound)
    solns = []
    #print(free_area)

    for i in data.data:

        i_id = i[0]
        i_w = i[1]
        i_h = i[2]

        poly_rep = Polygon.Shapes.Rectangle(i_w, i_h) #polygon representation of this shape, floating in space
        x, y = no_fill_polygon(total_area,free_area,poly_rep) #calculate position of polygon
        solns.append((i_id,x,y,i_w,i_h)) # add soln

        free_area = free_area - _create_rectangle(x,y,i_w,i_h) #calculate new free area
        free_area.simplify()
        #print(free_area)
        #Polygon.IO.writeSVG('test.svg', (free_area,))
        #break


    return skeleton.Solution(solns)