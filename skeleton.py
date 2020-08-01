from placement import *
from view import *
from neighbourhood import *

from random import randint
import time
from datetime import timedelta

class Data:
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


class Solution:
    """
    Soln format list of tuple [(id,posx,posy,width,height)]
    """

    soln = []

    def __init__(self,soln=None):
        self.soln = soln

    def verify(self):
        """
        Verify solution is correct, independent of internal representation of polygons in other methods
        :return: True if correct soln
        """
        i = 0
        j = 0

        while i < len(self.soln):
            while j < len(self.soln):
                if i != j:
                    check = self._overlap(self.soln[i],self.soln[j])
                    if check: # if overlap return false
                        return False
                j += 1
            i+=1
        return True #if no overlaps, return true

    def _overlap(self,rect1,rect2):
        """
        Chck if two rectangles overlap
        return true if overlap
        so want false
        :param rect1:
        :param rect2:
        :return:
        """
        a1 = rect1[1]
        a2 = rect1[3]+a1

        b1 = rect1[2]
        b2 = rect1[4]+b1

        c1 = rect2[1]
        c2 = rect2[3] + c1

        d1 = rect2[2]
        d2 = rect2[4] + d1

        #teest if a and c ranges overlap AND if b and d ranges overlap

        if (a2 >= c1 >= a1) or (a2 >= c2 >= a1):  #if x axis overlap
            if (b2 >= d1 >= b1) or (b2 >= d2 >= b1):
                return True
            if (d2 >= b1 >= d1) or (d2 >= b2 >= d1):
                return True

        if (c2 >= a1 >= c1) or (c2 >= a2 >= c1):  # if x axis overlap
            if (b2 >= d1 >= b1) or (b2 >= d2 >= b1):
                return True
            if (d2 >= b1 >= d1) or (d2 >= b2 >= d1):
                return True

        return False




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

def acceptance_basic(obj_incumbent, obj_challenger):
    return obj_challenger < obj_incumbent


class cutting_problem:
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
    """

    def __init__(self,file = None,debug_mode = False):
        self.data,self.width = load(file)
        self.debug_mode = debug_mode
        self.lowerbound = self.data.area/self.width
        self.upperbound = self.lowerbound * 4#claculat upper bound

        if(self.debug_mode):
            print("loaded", file)
            print("bounds are height:", self.upperbound, " width: ", self.width)


        self.solution = []

    def inital_solution(self):
        """
        Find an initial sequence
        :return:
        """

        sorted = self.data.data
        sorted.sort(key = lambda i: i[1]*i[2],reverse = True)
        self.data = Data(sorted)
        self.solution = self.place(self.data)
        print(self.solution.verify())




    def run(self,num_iterations=1000):
        """

        :return:
        """

        #Step 2: Generate initial soln
        self.inital_solution()

        if self.debug_mode:
            print("generated initial soln")

        #Step 3 iterate (with stopping criterion)
            #3.a Search
            #3.b Fill
        start_time = time.time()

        for i in range(0,num_iterations):
            self.data = self.search(self.data, neighbourhood_swap, acceptance_basic, False)
            self.solution = self.place(self.data)
        if self.debug_mode:
            print("generated final soln")

        executation_time = time.time()-start_time
        print("Took ", executation_time/1000, "seconds to execute")
        return self.solution

    def view(self):
        """
        #Step 4: Visualise soln
        :return:
        """
        view(self.solution,self.width,self.upperbound)

    def place(self, data):
        """
        Placement algorithm that takes a sequence of data and places them according to a heuristic
        :param data: data format list of tuple [(id,width,height)]
        :return:
        """
        return bottom_left_fill(data, self.width, self.upperbound,debug_mode=self.debug_mode)
        # return Solution()

    def search(self, data, neighbourhood_function, acceptance_function, first_improvement):
        """
        Search heuristic that takes a sequence of data and modifies them according to a neighbourhood
        :param data: data format list of tuple [(id,width,height)]
        :return:
        """
    
        initial_solution = self.place(data)
        neighbourhood = neighbourhood_function(self.data)
        best_obj = objective(initial_solution)
        best_sequence = data

        print("beginning search iteration")
        for sequence in neighbourhood:
            soln = self.place(sequence)
            next_obj = objective(soln)
            #print("Current objective: {} Next objective {}".format(best_obj,next_obj))
            #if acceptance function is fulfilled, replace best sequence
            if acceptance_function(best_obj, next_obj):
                print("Found improvement from {} to {}".format(best_obj, next_obj))
                best_obj = next_obj
                best_sequence = sequence
                if first_improvement:
                    return best_sequence

        print("No improvement found")
        return best_sequence
