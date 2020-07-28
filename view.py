from skeleton import *
import PIL.ImageDraw as ImageDraw
import PIL.Image as Image

def test_view():
    data, width = load("data\M1a.csv")
    solution = place_random(data,800,400)
    view(solution)
    return

def draw_rectangle(rectangle, drawer,width,height,scalex,scaley):
    # takes a rectangle (id,x_pos,y_pos,width,height) and
    # draws it using a drawing object and scales it
    # co-ordinates origin is bottom-left on drawing
    id = rectangle[0]
    x_pos = rectangle[1] * scalex
    y_pos = (height - rectangle[2]) * scaley
    width = rectangle[3] * scalex
    height = rectangle[4] * scaley
    # print("drawing: {} at ({},{})".format(id,rectangle[1],rectangle[2]))
    points = ((x_pos, y_pos), (x_pos + width, y_pos), (x_pos + width, y_pos + height), (x_pos, y_pos + height))
    drawer.polygon(points)
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

    for rect in rectangles:
        draw_rectangle(rect, drawer, width,height , SCALEX,SCALEY)

    image.show()
    return