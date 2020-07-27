from skeleton import *


def best_improvement(data, neighbourhood_function):
    """
    Takes a given sequence and calculates the neighbourhood of adjacent sequences using
    the given neighbourhood function, finding the solution which results in the lowest
    objective function value

    Parameters
    ----------
    data : TYPE
        DESCRIPTION.
    neighbourhood_function : TYPE
        DESCRIPTION.

    Returns
    -------
    best_sequence : TYPE
        DESCRIPTION.

    """
    neighbourhood = neighbourhood_function(data)
    initial_sequence = data
    initial_solution = place(data)
    best_obj = objective(solution)
    best_sequence = initial_sequence

    for sequence in neighbourhood:
        soln = place(sequence)
        objective_value = objective(soln)
        if objective_value < best_obj:
            best_obj = objective_value
            best_sequence = sequence

    return best_sequence


def first_improvement(data, neighbourhood_function):
    """
    Takes given sequence and finds the first solution of the given neighbourhood
    to improve upon the objective function

    Parameters
    ----------
    data : TYPE
        DESCRIPTION.
    neighbourhood_function : TYPE
        DESCRIPTION.

    Returns
    -------
    None.
    """

    neighbourhood = neighbourhood_function(data)
    initial_sequence = data
    initial_solution = place(data)
    intial_obj = objective(initial_solution)

    for sequence in neighbourhood:
        current_solution = place(sequence)
        next_obj = objective(current_solution)
        if next_obj < intial_obj:
            return sequence

    return initial_solution
