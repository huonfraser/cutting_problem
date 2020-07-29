import skeleton

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
        neighbourhood.append(new_sequence)

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

def neighbourhood_sample(neighbourhood, sample_rate):
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
    for i in range(0,len(neighbourhood)):
        if i%sample_rate == 0:
            sample.append(neighbourhood[i])
    return sample

