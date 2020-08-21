import Polygon  # library for handling polygons https://pypi.org/project/Polygon/#:~:text=Polygon%20is%20a%20python%20package,in%20a%20very%20intuitive%20way.
import Polygon.Shapes
import Polygon.IO
from Polygon.Utils import warpToOrigin
from random import randint
import main
import view


import datetime

def place_random(data, window_width, window_height):
    """
    Testing method, places rectangles in random places
    :param data:
    :param window_width:
    :param window_height:
    :return:
    """
    rectangles = data.data
    placed_rectangles = []

    for rect in rectangles:
        width = rect[1]
        height = rect[2]
        x_pos = randint(0, window_width - width)
        y_pos = randint(0, window_height - height)
        id = rect[0]

        placed_rectangles.append((id, x_pos, y_pos, width, height))

    return main.Solution(placed_rectangles)


def order_triangles(tri1):
    """
    Sorting criterion for triangles
    :param tri1:
    :return:
    """
    # triangle of format ((x1,y1),(x2,y2),(x3,y3)), where x1,y1 bottom left
    bottom_left = tri1[1]
    pre = int(bottom_left[1])
    suf = int(bottom_left[0])
    full = str(pre) + "." + str(suf)  # sort by y first then by x if y equal
    return (float(full))


def no_fill_polygon(area, poly1, poly2, debug_mode=False):
    """
    Return nfp of polygon 1 and polygon2, places around polygon 1 that polygon 2 can be placed
    :param area: area polygons are allowed to be placed in
    :param poly1: the free space polygon
    :param poly2: the polygon to be placed
    :return: position of the bottom left corner of the polygon
    """

    # search free free area for points
    # try bottom most left one where fits, nfp polygon

    # return x,y

    tristrip = poly1.triStrip()
    triangles = tristrip_to_triangles(tristrip)
    triangles.sort(key=order_triangles)  # order triangles by smallest x, smallest y if equal
    # print(triangles)

    filled_area = area - poly1

    area_bbox = area.boundingBox()
    for t in triangles:
        x, y = t[0]
        warpToOrigin(poly2)
        poly2.shift(x, y)
        # print(poly2)
        # if(poly1.covers(poly2)):
        if not poly2.overlaps(filled_area):
            poly_bbox = poly2.boundingBox()
            if poly_bbox[0] >= area_bbox[0] and poly_bbox[1] <= area_bbox[1] and poly_bbox[2] >= area_bbox[2] and poly_bbox[3] <= area_bbox[3]:

                if debug_mode:
                    print("can place at", x, y)
                    return x, y, triangles  # if debug also return triangles
                return x, y
        else:
            if debug_mode:
                print("clash")

        # else continue
    print("help")   # should never reach this point

    pass


def tristrip_to_triangles(tristrip, debug_mode=False):
    """
    Create triangles from the tristrips
    :param tristrip:
    :param debug_mode:
    :return:
    """
    triangles = []
    for tri in tristrip:
        for i in range(0, len(tri) - 2):
            val1 = (tri[i])
            val2 = (tri[i + 1])
            val3 = (tri[i + 2])
            # find bottom left triangle, order bottomleft,bottomright,top (do we ignore top right triangle)

            minx = min(min(val1[0], val2[0]), val3[0])
            miny = min(min(val1[1], val2[1]), val3[1])
            # print(minx,miny)
            if val1 == (minx, miny) or val2 == (minx, miny) or val3 == (minx, miny):  # ignore topright
                triangles.append((val1, val2, val3))

    # print(triangles)
    # view.view_triangle(triangles)

    return triangles


def _create_rectangle(x, y, width, height):
    """
    Helper method, creates a Rectangle
    :param x:
    :param y:
    :param width:
    :param height:
    :return:
    """
    return Polygon.Polygon([(x, y), (x + width, y), (x + width, y + height), (x, y + height), (x, y)])


def bottom_left_fill(data, width, upperbound, debug_mode=False, buffer=0):
    """
    Bottom left fill, places data inside the dimensions defined by width and upperbound
    :param data:
    :param width:
    :param upperbound:
    :param debug_mode:
    :param buffer:
    :return:
    """

    free_area = _create_rectangle(0, 0, width, upperbound)  # set available area
    total_area = _create_rectangle(0, 0, width, upperbound)
    solns = []

    for i in data.data:
        i_id = i[0]
        i_w = i[1] + buffer
        i_h = i[2] + buffer

        poly_rep = Polygon.Shapes.Rectangle(i_w, i_h)  # polygon representation of this shape, floating in space
        if debug_mode: #debugging method, step through placing one rectangle at a time
            x, y, triangles = no_fill_polygon(total_area, free_area, poly_rep, debug_mode=debug_mode)
            free_area = free_area - _create_rectangle(x, y, i_w, i_h)  # calculate new free area
            free_area.simplify()
            filled_area = total_area - free_area

            view.view_debug(solns, triangles, filled_area, width, upperbound)
        else:
            x, y = no_fill_polygon(total_area, free_area, poly_rep,
                                   debug_mode=debug_mode)  # calculate position of polygon
            free_area = free_area - _create_rectangle(x, y, i_w, i_h)  # calculate new free area
            free_area.simplify()
            filled_area = total_area - free_area

        solns.append((i_id, x, y, i_w - buffer, i_h - buffer))  # add soln


    return main.Solution(solns)
