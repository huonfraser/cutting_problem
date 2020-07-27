from placement import *
from view import *
from neighbourhood import *

from random import randint

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



class cutting_problem:

    def run(self,file):
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
        data,self.width = load(file)
        self.lowerbound = data.area/self.width
        self.upperbound = self.lowerbound * 4#claculat upper bound

        #Step 2: Generate initial soln
        solution = self.place(data,self.width,self.upperbound)

        #Step 3 iterate (with stopping criterion)
            #3.a Search
            #3.b Fill
        numIterations = 0
        for i in range(0,numIterations):
            data = self.search(data)
            solution = self.place(data,self.width,self.upperbound)

        #Step 4: Visualise soln
        view(solution)
        pass

    def place(self, data, width, upperbound):
        """
        Placement algorithm that takes a sequence of data and places them according to a heuristic
        :param data: data format list of tuple [(id,width,height)]
        :return:
        """
        return bottom_left_fill(data, width, upperbound)
        # return Solution()

    def search(data, neighbourhood_function, acceptence_function, placement_algorithm):
        """
        Search heuristic that takes a sequence of data and modifies them according to a neighbourhood
        :param data: data format list of tuple [(id,width,height)]
        :return:
        """
        return Data(data)


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
#test_view()
