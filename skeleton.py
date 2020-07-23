<<<<<<< HEAD
import Polygon #library for handling polygons https://pypi.org/project/Polygon/#:~:text=Polygon%20is%20a%20python%20package,in%20a%20very%20intuitive%20way.
import Polygon.Shapes
=======
import polygons #library for handling polygons https://pypi.org/project/Polygon/#:~:text=Polygon%20is%20a%20python%20package,in%20a%20very%20intuitive%20way.
import PIL.ImageDraw as ImageDraw
import PIL.Image as Image

>>>>>>> working
def view(solution):
    """
    Visualise a soln
    :param solution:
    :return:
    """
    image = Image.new("RGB", (640,480))
    draw = ImageDraw.Draw(image)
    rectangles = solution.data
    
    for rectangle in solution:
        id = rectangle[0]
        print("drawing"+str(id))
        #x_pos = rectangle[1]
        #y_pos = rectangle[2]
        width = rectangle[1]
        height = rectangle[2]
        points = ((0,0),(0,height),(height,width),(width,0))
        draw.polygon(points)
        
    image.show()    
    return

def bottom_left_fill(data, width,upperbound):
    #place each item in data, in order

    #generate a union polygon of placed, of size less than width
    #we can take disjoint set of this and width, and edges of this to generate NFP
    #we will need a no-fill-polygon for placement points

    roll_polygon = Polygon.Shapes.Rectangle(width,upperbound)
    filled_area = None
    free_area = roll_polygon / filled_area
    print(free_area)

    for i in data:

        i_id = i[0]
        i_x = i[1]
        i_y = i[2]




    pass


def load(file_name):
    """
    Load data from a file , return a sequence of soln and width of the file
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

def objective(soln):
    """Calculate waste, or minimize waste """
    return 0

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

<<<<<<< HEAD
=======
data = load("data\M1a.csv")
>>>>>>> working
