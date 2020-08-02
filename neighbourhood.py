import skeleton
from random import randint

def neighbourhood_rotate(data):
    """
    Generates neighbourhood adjacent to sequence from all possible single element rotations
    A rotation swaps height and width

    Parameters
    ----------
    data : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """

    neighbourhood = []
    rectangles = data.data
    for i in range(0, len(rectangles)):
        new_sequence = rectangles.copy()
        rect = rectangles[i]
        id = rect[0]
        width = rect[1]
        height = rect[2]
        rectangles[i] = (id, height, width)
        neighbourhood.append(skeleton.Data(new_sequence))

    return neighbourhood


def neighbourhood_swap(data):
    # generates neighbourhood of all sequences from all possible single element swaps
    neighbourhood = []
    rectangles = data.data
    for i in range(0, len(rectangles)):
        for j in range(i + 1, len(rectangles) - 1):
            new_sequence = rectangles.copy()
            temp1 = new_sequence[i]
            temp2 = new_sequence[j]
            new_sequence[i] = temp2
            new_sequence[j] = temp1
            neighbourhood.append(skeleton.Data(new_sequence))

    return neighbourhood


def neighbourhood_insert(data):
    # generates neighbourhood of all sequences from all possible single element insertions
    neighbourhood = []
    rectangles = data.data
    for i in range(0, len(rectangles)):
        for j in range(0, len(rectangles)):
            # cannot insert element into its original position
            if i == j:
                continue
            # copy fresh unaltered sequence, then perform insertion of element
            new_sequence = rectangles.copy()
            temp = new_sequence.pop(i)
            new_sequence.insert(j, temp)
            neighbourhood.append(skeleton.Data(new_sequence))

    return neighbourhood

def neighbourhood_sample(neighbourhood, sample_proportion):
    """
    Takes a neighbourhood and samples sequences at a given interval
    Should be replaced by a random sampler of some sort

    Parameters
    ----------
    neighbourhood : TYPE
        DESCRIPTION.
    sample_rate : TYPE
        DESCRIPTION.

    Returns
    -------
    sample : TYPE
        DESCRIPTION.

    """
    sample = []
    size = len(neighbourhood)
    sample_number = (int)(len(neighbourhood)*sample_proportion)
    
    
    for i in range(0,sample_number):
        sampled_sequence = neighbourhood[randint(0,size-1)]
        sample.append(sampled_sequence)
    return sample

def highest_rectangle(rectangles):
    index_highest = 0
    highest = 0
    for i in range(0,len(rectangles)):
        y_pos = rectangles[i][2]
        if y_pos > highest:
            highest = y_pos
            index_highest = i
    return index_highest

def shake_insert(data):
    #returns a random sequence by single element insertion
    new_sequence = data.data.copy()
    sequence_length = len(new_sequence)
    element_index = randint(0,sequence_length-1)
    new_position = randint(0,sequence_length-1)
    temp = new_sequence.pop(element_index)
    new_sequence.insert(new_position,temp)
    #print("Shaking {} {}".format(element_index,new_position))
    
    return skeleton.Data(new_sequence)
    

def shake_swap(data):
    #returns a random sequence by swapping two elements
    #in the given sequence
    new_sequence = data.data.copy()
    sequence_length = len(new_sequence)
    i = randint(0,sequence_length-1)
    j = randint(0,sequence_length-1)
    temp1 = new_sequence[i]
    temp2 = new_sequence[j]
    new_sequence[i] = temp2
    new_sequence[j] = temp1
    #print("Swapping {} {}".format(i, j))
    return skeleton.Data(new_sequence)

def shake_rotate(data):
    #returns a random sequence by rotating a random element
    #in the given sequence
    new_sequence = data.data.copy()
    sequence_length = len(new_sequence)
    i = randint(0,sequence_length-1)
    rect = new_sequence[i]
    id = rect[0]
    width = rect[1]
    height = rect[2]
    new_sequence[i] = (id, height, width)
    #print("Rotating {}".format(i))
    
    return skeleton.Data(new_sequence)
    
    
    

# =============================================================================
# def random_insert(data):
#     pass
# 
# def random_swap(data):
#     pass
# def random_rotate(data):
#     pass
# =============================================================================
    
    

