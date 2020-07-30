from skeleton import *
import PIL.ImageDraw as ImageDraw
from colour import Color
from tkinter import Canvas, Tk, PhotoImage
from PIL import Image


def test_view():
    data, width = load("data\M1a.csv")
    solution = place_random(data,800,400)
    view(solution)
    return

def view_debug(solution,triangles,width,height):
    """

    :param rectangles:
    :param triangles:
    :param width:
    :param height:
    :return:
    """
    WINDOW_HEIGHT = 800
    WINDOW_WIDTH = 800
    SCALEX = WINDOW_WIDTH/width
    SCALEY = WINDOW_HEIGHT/height

    image = Image.new("RGB", (WINDOW_WIDTH, WINDOW_HEIGHT))
    drawer = ImageDraw.Draw(image)
    rectangles = solution

    if len(rectangles)>0:
        red = Color("red")
        colors = list(red.range_to(Color("green"), len(rectangles)))
    for i in range(0,len(rectangles)):
        rect = rectangles[i]
        colour = colors[i].rgb
        r = int(colour[0]*255)
        g = int(colour[1]*255)
        b = int(colour[2]*225)
        draw_rectangle(rect, drawer, width,height, SCALEX,SCALEY,(r,g,b))

    for tri in triangles:
        draw_triangle(tri, drawer, width,height, SCALEX,SCALEY)

    image.show()

def draw_triangle(triangle,drawer,window_width,window_height,scalex,scaley):
    p1 = triangle[0]
    p2 = triangle[1]
    p3 = triangle[2]

    points = (p1[0]*scalex,(window_height-p1[1])*scaley),(p2[0]*scalex,(window_height-p2[1])*scaley),(p3[0]*scalex,(window_height- p3[1])*scaley)
    drawer.polygon(points,)
    return

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
        draw_triangle(tri, drawer, width,height, SCALEX,SCALEY)


    image.show()
    return



def draw_rectangle(rectangle, canvas,window_width,window_height,scalex,scaley,fill):
    # takes a rectangle (id,x_pos,y_pos,width,height) and
    # draws it using a drawing object and scales it
    # co-ordinates origin is bottom-left on drawing
    id = rectangle[0]
    x_pos = rectangle[1] * scalex
    y_pos = (window_height - rectangle[2]) * scaley
    width = rectangle[3] * scalex
    height = rectangle[4] * scaley
    # print("drawing: {} at ({},{})".format(id,rectangle[1],rectangle[2]))
    points = ((x_pos, y_pos), (x_pos + width, y_pos), (x_pos + width, y_pos - height), (x_pos, y_pos - height))
    canvas.create_rectangle(x_pos,y_pos-height,x_pos+width,y_pos, fill =fill,outline = "black")
    return


def view(solution,width,height):
    """
    Visualise a soln
    :param solution:
    :return:
    """
    WINDOW_HEIGHT = 800
    WINDOW_WIDTH = 800
    SCALEX = WINDOW_WIDTH/width
    SCALEY = WINDOW_HEIGHT/height

    image = Image.new("RGB", (WINDOW_WIDTH, WINDOW_HEIGHT))
    drawer = ImageDraw.Draw(image)
    rectangles = solution.soln

    window = Tk()

    c = Canvas(window, width=WINDOW_WIDTH, height=WINDOW_WIDTH)
    c.pack()

    c.create_rectangle(0,0,WINDOW_WIDTH,WINDOW_HEIGHT,outline = "black")

    red = Color("red")
    colors = list(red.range_to(Color("green"), len(rectangles)))
    for i in range(0,len(rectangles)):
        rect = rectangles[i]
        colour = colors[i].hex
        #r = int(colour[0]*255)
        #g = int(colour[1]*255)
        #b = int(colour[2]*225)
        draw_rectangle(rect, c, width,height, SCALEX,SCALEY,colour)

    window.mainloop()

    #image.show()
    return