import Polygon #library for handling polygons https://pypi.org/project/Polygon/#:~:text=Polygon%20is%20a%20python%20package,in%20a%20very%20intuitive%20way.
import Polygon.Shapes
import PIL.ImageDraw as ImageDraw
import PIL.Image as Image
from random import randint

def draw_rectangle(rectangle, drawer, window_height, scale):
    #takes a rectangle (id,x_pos,y_pos,width,height) and
    #draws it using a drawing object and scales it 
    #co-ordinates origin is bottom-left on drawing
    id = rectangle[0]
    x_pos = rectangle[1]*scale
    y_pos = (window_height-rectangle[2])*scale
    width = rectangle[3]*scale
    height = rectangle[4]*scale
    #print("drawing: {} at ({},{})".format(id,rectangle[1],rectangle[2]))
    points = ((x_pos,y_pos),(x_pos+width,y_pos),(x_pos+width,y_pos+height),(x_pos,y_pos+height))
    print(points)
    drawer.polygon(points)

def view(solution):
    """
    Visualise a soln
    :param solution:
    :return:
    """
    WINDOW_HEIGHT = 800
    WINDOW_WIDTH = 400
    SCALE = 2

    image = Image.new("RGB", (WINDOW_WIDTH*SCALE,WINDOW_HEIGHT))
    drawer = ImageDraw.Draw(image)
    rectangles = solution.soln
    
    for rect in rectangles:
        draw_rectangle(rect, drawer, WINDOW_HEIGHT, SCALE)
        
    image.show()    
    return

def place_random(data, window_height, window_width):
    rectangles = data.data
    placed_rectangles = []
    for rect in rectangles:
        x_pos = randint(0,window_width)
        y_pos = randint(0,window_height)
        id = rect[0]
        width = rect[1]
        height = rect[2]
        placed_rectangles.append((id,x_pos,y_pos,width,height))
    
    return Solution(placed_rectangles)

def no_fill_polygon(poly1,poly2):
    """
    Return nfp of polygon 1 and polygon2, places around polygon 1 that polygon 2 can be placed
    :param poly1: the free space polygon
    :param poly2: the polygon to be filled
    :return: position of the bottom left corner of the polygon
    """


    # search free free area for points
    # try bottom most left one where fits, nfp polygon

    #return x,y
    pass


def _create_rectangle(x,y,width,height):
    return Polygon.Polygon([(x,y),(x+width,y),(x+width,y+height),(x,y+height),(x,y)])


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



def load(file_name):
    """
    Load data from a file, return a sequence of soln and width of the file
    :param file_name:
    :return: Loaded instanc

    data format list of tuple [(id,width,height)]
    """
    data = []
    with open(file_name, "r") as file:
        line1 = file.readline().replace("\n","") #size line
        line2 = file.readline().replace("\n","") #area line
        line3 = file.readline() #col names file
        #print(line1)
        #print(line2)
        #print(line3)
        area = float(line2.split(",")[1])
        size = float(line1.split(",")[1])
        #print(area,size)
        content_lines = file.readlines()
        for line in content_lines:
            line = line.replace("\n","")
            splat = line.split(",",)
            data.append((float(splat[0]),float(splat[1]),float(splat[2])))
        #print(data)
    return Data(data, area), size

def neighbourhood_swap(data):
    #generates neighbourhood of all sequences from all possible single element swaps
    neighbourhood = []
    rectangles = data.data
    for i in range(0,len(rectangles)):
        for j in range(i+1,len(rectangles)-1):
            new_sequence = rectangles.copy()
            temp1 = new_sequence[i]
            temp2 = new_sequence[j]
            new_sequence[i] = temp2
            new_sequence[j] = temp1
            neighbourhood.append(new_sequence)
    
    return Data(neighbourhood)

def neighbourhood_insert(data):
    #generates neighbourhood of all sequences from all possible single element insertions
    neighbourhood = []
    rectangles = data.data
    for i in range(0,len(rectangles)):
        for j in range(0,len(rectangles)):
            if i==j:
                continue
            #copy fresh unaltered sequence, then perform insertion of element
            new_sequence = rectangles.copy()
            temp = new_sequence.pop(i)
            new_sequence.insert(j,temp)
            neighbourhood.append(new_sequence)
            
    return Data(neighbourhood)

def objective(soln):
    """Calculate waste, or minimize waste """
    #Calculates height of solution by finding the highest placed block
    rectangles = soln.soln
    highest_point = 0
    for rect in rectangles:
        pos_y = rect[2]
        if pos_y > highest_point:
            highest_point = pos_y
        
    return highest_point

def optimal_improvement(data, neighbourhood_function):
    neighbourhood = neighbourhood_function(data)
    best_sequence = data
    best_obj = objective(data)
    pass

def first_improvement(data, neighbourhood_function):
    pass

def search(data):
    """
    Search heuristic that takes a sequence of data and modifies them according to a neighbourhood
    :param data: data format list of tuple [(id,width,height)]
    :return:
    """
    return Data(data)

def place(data,width,upperbound):
    """
    Placement algorithm that takes a sequence of data and places them according to a heuristic
    :param data: data format list of tuple [(id,width,height)]
    :return:
    """
    pass
    #return Solution()



def run(file):
    """
    Run a local search algorithm:
    Has the following elements:
    1. Loading function
    2. Initial soln generator
    3. Stopping criteria
    4. Placement heuristic
    5. Search heuristic
    6. Output viewer
    7. Objective function
    :return:
    """
    #Step 1: Load
    data,width = load(file)
    lowerbound = data.area/width
    upperbound = lowerbound * 4#claculat upper bound



    #Step 2: Generate initial soln
    solution = place(data,width,upperbound)

    #Step 3 iterate (with stopping criterion)
        #3.a Search
        #3.b Fill
    numIterations = 0
    for i in range(0,numIterations):
        data = search(data)
        solution = place(data,width,upperbound)

    #Step 4: Visualise soln
    view(solution)

    pass


class Data():
    """
    Holder class for input data set,
    represent a sequence of data

    data format list of tuple [(id,width,height)]
    """

    data = []
    area = 0


    def __init__(self, data, area=None):
        self.data = data
        if(area == None):
            #calculate area
            pass
        else:
            self.area = area


class Solution():
    """
    Soln format list of tuple [(id,posx,posy,width,height)]
    """

    soln = []

    def __init__(self,soln=None):
        self.soln = soln
    """
    Holder class for soln representation
    """

#design choice, - represent soln and data as seperate lists, vs single

data = load("data\M1a.csv")
