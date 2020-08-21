from main import *
import PIL.ImageDraw as ImageDraw
from colour import Color
from tkinter import Canvas, Tk, PhotoImage
from PIL import Image


def test_view():
    data, width = load("data\M1a_short3.csv")
    solution = place_random(data,800,400)
    view(solution)
    return

def view_debug(solution,triangles,polygon,width,height):
    """
    :param rectangles:
    :param triangles:
    :param width:
    :param height:
    :return:
    """
    WINDOW_HEIGHT = 800
    WINDOW_WIDTH = 800
    SCALEX = min(WINDOW_WIDTH/width,WINDOW_HEIGHT/height)
    SCALEY = min(WINDOW_WIDTH/width,WINDOW_HEIGHT/height)
    window = Tk()
    rectangles = solution

    c = Canvas(window, width=WINDOW_WIDTH, height=WINDOW_WIDTH)
    c.pack()

    c.create_rectangle(1, 1, WINDOW_WIDTH-1, WINDOW_HEIGHT-1, outline="white")



    if len(rectangles) > 0:
        red = Color("red")
        colors = list(red.range_to(Color("green"), len(rectangles)))
    for i in range(0,len(rectangles)):
        rect = rectangles[i]
        colour = colors[i].hex
        draw_rectangle(rect, c, width,height, SCALEX,SCALEY,colour)
        pass

    for tri in triangles:
        #draw_triangle(tri, c, WINDOW_WIDTH,WINDOW_HEIGHT, SCALEX,SCALEY)
        pass

    draw_polygon(polygon, c, WINDOW_WIDTH, WINDOW_HEIGHT, SCALEX, SCALEY)
    window.mainloop()

def draw_polygon(polygon, canvas, window_width, window_height, scalex, scaley):
    print(len(polygon))
    for p in polygon:
        for i in range(0,len(p)-1):
            p1 = p[i]
            p2 = p[i+1]

            x1 = p1[0]*scalex
            y1 = p1[1]*scaley

            x2 = p2[0]*scalex
            y2 = p2[1]*scaley


            canvas.create_line(x1,window_height-y1,x2,window_height-y2)

        p1 = p[0]
        p2 = p[len(p)-1]

        x1 = p1[0]*scalex
        y1 = p1[1]*scaley

        x2 = p2[0]*scalex
        y2 = p2[1]*scaley


        canvas.create_line(x1,window_height-y1,x2,window_height-y2)

    pass






def view_triangle(triangles):
    WINDOW_HEIGHT = 800
    WINDOW_WIDTH = 800
    width = 100
    height = 100.8
    SCALEX = WINDOW_WIDTH/width
    SCALEY = WINDOW_HEIGHT/height

    image = Image.new("RGB", (WINDOW_WIDTH, WINDOW_HEIGHT))
    drawer = ImageDraw.Draw(image)

    for tri in triangles:
        draw_triangle(tri, drawer, WINDOW_WIDTH,WINDOW_HEIGHT, SCALEX,SCALEY)

    image.show()
    return


def draw_triangle(triangle, canvas, window_width, window_height, scalex, scaley):
    p1 = triangle[0]
    p2 = triangle[1]
    p3 = triangle[2]
    print(p1, p2, p3)

    x1 = p1[0]*scalex
    y1 =(p1[1])*scaley

    x2 = p2[0]*scalex
    y2 = p3[1]*scaley

    width = x2-x1
    height = y2-y1
    print("points",x1,y1,x2,y2)
    print("coords",x1,y1,width,height)

    if int(x1) == 0:
        x1 += 1

    if x2 == window_width:
        x2 -= 1

    if window_height - y2 == 0:
        y2 -= 1


    canvas.create_rectangle(x1, window_height-y2, x2, window_height-y1, outline="black")
    return

def draw_rectangle(rectangle, canvas,window_width,window_height,scalex,scaley,fill):
    # takes a rectangle (id,x_pos,y_pos,width,height) and
    # draws it using a drawing object and scales it
    # co-ordinates origin is bottom-left on drawing
    id = rectangle[0]
    x_pos = rectangle[1] * scalex
    y_pos = window_height - rectangle[2] * scaley
    width = rectangle[3] * scalex
    height = rectangle[4] * scaley
    # print("drawing: {} at ({},{})".format(id,rectangle[1],rectangle[2]))
    canvas.create_rectangle(x_pos,y_pos-height,x_pos+width,y_pos, fill =fill,outline = "White")
    return


def view(solution, width, height):
    """
    Visualise a soln with problem dimensions givn by width and height
    :param height:
    :param width:
    :param solution:
    :return:
    """
    WINDOW_HEIGHT = 800.0
    WINDOW_WIDTH = 800.0
    height = height*1.0
    width = width*1.0

    SCALEX = min(WINDOW_WIDTH/width, WINDOW_HEIGHT/height)
    SCALEY = min(WINDOW_WIDTH/width, WINDOW_HEIGHT/height)

    rectangles = solution.soln

    window = Tk()

    c = Canvas(window, width=WINDOW_WIDTH, height=WINDOW_WIDTH)
    c.pack()

    #draw region that can be filled
    c.create_rectangle(0.0, WINDOW_HEIGHT-height*SCALEY, width*SCALEX, WINDOW_HEIGHT, fill="black", outline="black")

    red = Color("red")
    colors = list(red.range_to(Color("green"), len(rectangles)))
    for i in range(0,len(rectangles)):
        rect = rectangles[i]
        colour = colors[i].hex
        #r = int(colour[0]*255)
        #g = int(colour[1]*255)
        #b = int(colour[2]*225)
        draw_rectangle(rect, c, WINDOW_WIDTH, WINDOW_HEIGHT, SCALEX, SCALEY, colour)

    window.mainloop()

    #image.show()
    return