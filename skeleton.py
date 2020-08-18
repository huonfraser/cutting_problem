from placement import *
from view import *
from neighbourhood import *

from random import randint

import datetime
import time


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
            self.area=self.calc_area()
            pass
        else:
            self.area = area

    def calc_area(self):
        total = 0

        for d in self.data:
            #print("{}, {}".format(d[1],d[2]))
            total += d[1]*d[2]

        return total


class Solution:
    """
    Soln format list of tuple [(id,posx,posy,width,height)]
    """

    soln = []

    def __init__(self,soln=None):
        self.soln = soln

    def verify(self,width = None,height = None):
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

        #check lie insid bounds if width and height != None
        for rect in self.soln:
            if(rect[1] < 0):
                return False
            if(width != None):
                if rect[1]+rect[3] > width:
                    return False

            if (rect[2] < 0):
                return False
            if (height != None):
                if rect[2] + rect[4] > width:
                    return False

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
    """Calculate waste, or minimize height"""
    #Calculates height of solution by finding the highest placed block
    rectangles = soln.soln
    highest_point = 0
    for rect in rectangles:
        pos_y = rect[2]+rect[4]
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

    def __init__(self,file=None, debug_mode=False, buffer=0.0, sort_criteria="area", rotate_criteria="none", neighbourhood_functions = []):
        self.data, self.width = load(file)
        self.debug_mode = debug_mode
        self.lowerbound = self.data.area/self.width
        self.upperbound = self.lowerbound * 2 #claculat upper bound

        self.sort_criteria = sort_criteria
        self.rotate_criteria = rotate_criteria
        
        self.neighbourhood_functions = neighbourhood_functions

        self.buffer = buffer

        self.placement_times = []
        self.placements_searched = 0

        if(self.debug_mode):
            print("loaded", file)
            print("bounds are height:", self.upperbound, " width: ", self.width)

        self.solution = []

    def initial_solution(self,sort_criteria="none", rotate_criteria="none"):
        """
        Find an initial sequence
        :return:
        """

        sorted = self.data.data

        if rotate_criteria == "none":
            pass #leave as is
        elif rotate_criteria == "down":
            sorted = [(lambda x: (x[0],x[2],x[1]) if x[1] < x[2] else x)(i) for i in sorted]
            pass #rotate so that width > height
        elif rotate_criteria == "up": #rotate st
            sorted = [(lambda x: (x[0],x[2],x[1]) if x[1] > x[2] else x)(i) for i in sorted]

        if sort_criteria == "none":
            pass
        elif sort_criteria == "area":
            sorted.sort(key=lambda i: i[1]*i[2], reverse=True)
        elif sort_criteria == "width":
            sorted.sort(key=lambda i: i[1], reverse=True)
        elif sort_criteria == "height":
            sorted.sort(key=lambda i: i[2], reverse=True)
        elif sort_criteria == "max":
            sorted.sort(key=lambda i: max(i[1], i[2]), reverse=True)
        elif sort_criteria == "min":
            sorted.sort(key=lambda i: min(i[1], i[2]), reverse=True)

        self.data = Data(sorted)
        self.solution = self.place(self.data)

        print("Initial solution generated with height", objective(self.solution))

    def search(self):
        return self.variable_neighbourhood_descent(self.data, neighbourhoods=self.neighbourhood_functions)

    def run(self):
        """

        :return: solution, height average placement time, number of placements searched
        """

        #Step 2: Generate initial soln

        self.placements_searched = 0
        self.placement_times = []

        self.initial_solution(rotate_criteria=self.rotate_criteria, sort_criteria=self.sort_criteria)
        if self.debug_mode:
            print("generated initial soln")

        #Search
        start = time.clock()
        self.data = self.search()
        end = time.clock()
        search_time = end - start
        self.solution = self.place(self.data)
        final_height = objective(self.solution)

        if self.debug_mode:
            print("generated final soln")

        print("final height value is ", final_height)
        waste = 1.0-(self.data.calc_area())/(final_height*self.width)
        print("Waste is " + str(waste))

        avg_time = sum(self.placement_times)/len(self.placement_times)
        print("Search took {} seconds".format(search_time))
        print("Average placement time was {} milliseconds".format(avg_time*1000))
        print("Number of placements searched was {} ".format(self.placements_searched))
        return self.solution,final_height, avg_time, self.placements_searched

    def view(self):
        """
        #Step 4: Visualise soln
        :return:
        """
        view(self.solution, self.width, self.upperbound)

    def place(self, data):
        """
        Placement algorithm that takes a sequence of data and places them according to a heuristic

        Record time
        :param data: data format list of tuple [(id,width,height)]
        :return:
        """
        start_time = time.clock()


        solution = bottom_left_fill(data, self.width, self.upperbound, debug_mode=self.debug_mode, buffer=self.buffer)
        end_time = time.clock()
        run_time = end_time - start_time
        self.placement_times.append(run_time) # time in microseconds
        return solution
        # return Solution()

    def search_neighbourhood(self, data, neighbourhood_function, acceptance_function=acceptance_basic, first_improvement=True):
        """
        Search heuristic that takes a sequence of data and modifies them according to a neighbourhood
        :param first_improvement:
        :param acceptance_function:
        :param neighbourhood_function:
        :param data: data format list of tuple [(id,width,height)]
        :return:
        """
        #keep track of previous, best solution
        initial_sequence = data
        initial_solution = self.place(initial_sequence)
        initial_objective = objective(initial_solution)
        
        neighbourhood = neighbourhood_function(data)
        length = len(neighbourhood)
        print("Neighbourhood of size {} ".format(length))
        self.placements_searched +=length

        #keep track of best solution found in this neighbourhood
        best_sequence = neighbourhood[0]
        best_solution = self.place(data)
        best_obj = objective(best_solution)

        #print("beginning search iteration")
        for i in range(1, length):
            #if i%100 == 0:
                #print("Searched {} out of {}".format(i,length))
            #sys.stdout.write("Searched {} out of {}\r".format(i,length))
            #sys.stdout.flush()
            
            next_sequence = neighbourhood[i]
            next_soln = self.place(next_sequence)
            next_obj = objective(next_soln)
            
            #if acceptance function is fulfilled, replace best sequence
            if acceptance_function(best_obj, next_obj):
                print("Best solution in neighbourhood improved from {} to {}".format(best_obj, next_obj))
                best_obj = next_obj
                best_sequence = next_sequence
                best_solution = next_soln

                if first_improvement and best_obj < initial_objective:
                    return best_sequence

        #print("No improvement found")
        return best_sequence
    
    def neighbourhood_change(self, current_sequence, next_sequence, k):
        """
        If solution is better, reset to first neighbourhood function.
        If solution is same or worse, increment k to move to next function 

        :param current_sequence: Current best solution
        :param compare_sequence: Best solution in current neighbourhood
        :param k: Neighbourhood function index
        :return: Improved slutin and a k
        """
        #Calculate performance of given sequences
        current_solution = self.place(current_sequence)
        current_obj = objective(current_solution)

        next_solution = self.place(next_sequence)
        next_obj = objective(next_solution)

        if next_obj < current_obj: #neighbourhood gave a better solution
            print("Neighbourhood {} improved from {} to {}".format(k, current_obj, next_obj))
            return next_sequence, 1
        else:
            print("Neighbourhood {} saw no improvement".format(k))
            return current_sequence, k+1
        
   

    def variable_neighbourhood_descent(self, data, neighbourhoods=[]):
        """
        Implementation of Variable Neighbourhood Descent, which iterates through a given list of neighbourhood functions.
        Each time an improvement on the current solution is found, it resets back to the first neighbourhood.
        :param neighbourhoods: List of neighbourhood functions
        :param data: Initial sequence to start search
        :return:
        """
        k_max = len(neighbourhoods)
        #Set the initial sequence as the best sequence
        best_sequence = data
        
        k = 0
        
        while k < k_max: #iterate until no improvements in any neighbourhood
            print("searching {}".format(neighbourhoods[k].__name__))
           
            compare_sequence = self.search_neighbourhood(best_sequence, neighbourhoods[k], acceptance_basic, False)
            best_sequence, k = self.neighbourhood_change(best_sequence, compare_sequence, k)
            
        print("Finished VND")
        return best_sequence

        