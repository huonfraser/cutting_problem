from skeleton import *
import PIL.ImageDraw as ImageDraw
import PIL.Image as Image

def test_view():
    data, width = load("data\M1a.csv")
    solution = place_random(data,800,400)
    view(solution)
    return

def draw_rectangle(rectangle, drawer, window_height, scale):
    # takes a rectangle (id,x_pos,y_pos,width,height) and
    # draws it using a drawing object and scales it
    # co-ordinates origin is bottom-left on drawing
    id = rectangle[0]
    x_pos = rectangle[1] * scale
    y_pos = (window_height - rectangle[2]) * scale
    width = rectangle[3] * scale
    height = rectangle[4] * scale
    # print("drawing: {} at ({},{})".format(id,rectangle[1],rectangle[2]))
    points = ((x_pos, y_pos), (x_pos + width, y_pos), (x_pos + width, y_pos + height), (x_pos, y_pos + height))
    drawer.polygon(points)
    return


def view(solution):
    """
    Visualise a soln
    :param solution:
    :return:
    """
    WINDOW_HEIGHT = 800
    WINDOW_WIDTH = 400
    SCALE = 2

    image = Image.new("RGB", (WINDOW_WIDTH * SCALE, WINDOW_HEIGHT))
    drawer = ImageDraw.Draw(image)
    rectangles = solution.soln

    for rect in rectangles:
        draw_rectangle(rect, drawer, WINDOW_HEIGHT, SCALE)

    image.show()
    return