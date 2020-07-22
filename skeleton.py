import polygons #library for handling polygons https://pypi.org/project/Polygon/#:~:text=Polygon%20is%20a%20python%20package,in%20a%20very%20intuitive%20way.


def view(solution):
    """
    Visualise a soln
    :param solution:
    :return:
    """
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
        line1 = file.readline() #size line
        line2 = file.readline() #area line
        line3 = file.readline() #col names file
        #print(line1)
        #print(line2)
        #print(line3)
        area = line2.split(",")[1]
        content_lines = file.readlines()
        for line in content_lines:
            line = line.replace("\n","")
            splat = line.split(",",)
            data.append((splat[0],splat[1],splat[2]))
        print(data)
    return Data(data, area), 0

def search(data):
    """
    Search heuristic that takes a sequence of data and modifies them according to a neighbourhood
    :param data: data format list of tuple [(id,width,height)]
    :return:
    """
    return Data(data)

def place(data):
    """
    Placement algorithm that takes a sequence of data and places them according to a heuristic
    :param data: data format list of tuple [(id,width,height)]
    :return:
    """
    return Solution()

def objective(soln):
    """Calculate waste, or minimize waste """
    return 0

def run():
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
    data,width = load("xyz")



    #Step 2: Generate initial soln
    solution = place(data)

    #Step 3 iterate (with stopping criterion)
        #3.a Search
        #3.b Fill
    numIterations = 0
    for i in range(0,numIterations):
        data = search(data)
        solution = place(data)

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

    def __init__(self,soln):
        self.soln = soln
    """
    Holder class for soln representation
    """

#design choice, - represent soln and data as seperate lists, vs single

load("data\M1a.csv")