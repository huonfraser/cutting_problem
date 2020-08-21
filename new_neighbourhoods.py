# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 16:08:28 2020

@author: albib
"""

import main

def swap(data, i1, i2):
    """
    swaps two elements

    Parameters
    ----------
    data : TYPE
        DESCRIPTION.
    i1 : TYPE
        DESCRIPTION.
    i2 : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    temp = data[i1]
    data[i1] = data[i2]
    data[i1] = temp


def swap_adjacent(sequence, n_swaps, start):
    """
    performs n adjacent swaps on the given sequence starting at the given position

    Parameters
    ----------
    data : TYPE
        DESCRIPTION.
    n : TYPE int
        DESCRIPTION.
        number of adjacent swaps to make

    Returns
    list which has been altered through a series of adjacent element swaps
    -------
    None.

    """
    end = start + n_swaps*2
    for i in range(start, end, 2):
        swap(sequence,i,i+1)

def swap_adjacent_block(sequence, n_swaps, start):
    """
    performs an adjacent block swap of n elements

    Parameters
    ----------
    sequence : TYPE
        DESCRIPTION.
    n_swaps : TYPE
        DESCRIPTION.
    start : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    
    end = start + n_swaps
    for i in range(start, end):
        #print(end)
        #print(str(i+n_swaps))
        swap(sequence, i, i+n_swaps)
    
    return sequence

    
        
     
def nh_swap_adjacent(data, n_swaps):
    """
    Generates the neighbourhood of all sequences from performing n adjacent swaps

    Parameters
    ----------
    sequence : TYPE
        DESCRIPTION.
    n_swaps : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    sequence = data.data
    nh = []
    last = len(sequence)-n_swaps*2
    for i in range(0, last):
        nh_element = sequence.copy()
        swap_adjacent(nh_element, n_swaps, i)
        nh.append(main.Data(nh_element))
    
    return nh

def nh_swap_adjacent_block(data, n_elements):
    """
    Generates the neighbourhood of all sequences from performing n block swaps of elements

    Parameters
    ----------
    sequence : TYPE
        DESCRIPTION.
    n_swaps : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    sequence = data.data
    nh = []
    last = len(sequence) - n_elements*2
    for i in range(0, last):
        nh_element = sequence.copy()
        swap_adjacent_block(nh_element, n_elements, i)
        nh.append(main.Data(nh_element))
        #print(nh_element)
    
    return nh

def rotate_adjacent(sequence, n_elements, start):
    """
    Rotates a continuous block of elements

    Parameters
    ----------
    sequence : TYPE
        DESCRIPTION.
    n_elements : TYPE
        DESCRIPTION.
    start : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    for i in range(start, start+n_elements):
        rect = sequence[i]
        id = rect[0]
        width = rect[1]
        height = rect[2]
        sequence[i] = id, height, width
    

def nh_rotate_adjacent(data, n_elements):
    sequence = data.data
    nh = []
    last = len(sequence) - n_elements + 1
    for i in range(0,last):
        nh_element = sequence.copy()
        rotate_adjacent(nh_element, n_elements, i)
        nh.append(main.Data(nh_element))
    
    return nh

def shift_left(sequence, shift):
    length = len(sequence)
    shifted = sequence[shift:length].copy()
    shifted.append(sequence[0:shift].copy())
    return shifted

def nh_swap1(data):
    return nh_swap_adjacent(data, 1)

def nh_swap2(data):
    return nh_swap_adjacent(data, 2)

def nh_swap3(data):
    return nh_swap_adjacent(data, 3)

def nh_swap4(data):
    return nh_swap_adjacent(data, 4)

def nh_swap5(data):
    return nh_swap_adjacent(data, 5)

def nh_swap6(data):
    return nh_swap_adjacent(data, 6)

def nh_swap7(data):
    return nh_swap_adjacent(data, 7)

def nh_swap8(data):
    return nh_swap_adjacent(data, 8)

def nh_swap9(data):
    return nh_swap_adjacent(data, 9)

def nh_swap10(data):
    return nh_swap_adjacent(data, 10)

def nh_block1(data):
    return nh_swap_adjacent_block(data, 1)

def nh_block2(data):
    return nh_swap_adjacent_block(data, 2)

def nh_block3(data):
    return nh_swap_adjacent_block(data, 3)

def nh_block4(data):
    return nh_swap_adjacent_block(data, 4)

def nh_block5(data):
    return nh_swap_adjacent_block(data, 5)

def nh_block6(data):
    return nh_swap_adjacent_block(data, 6)

def nh_block7(data):
    return nh_swap_adjacent_block(data, 7)

def nh_block8(data):
    return nh_swap_adjacent_block(data, 8)

def nh_block9(data):
    return nh_swap_adjacent_block(data, 9)

def nh_block10(data):
    return nh_swap_adjacent_block(data, 10)

def nh_rotate1(data):
    return nh_rotate_adjacent(data, 1)

def nh_rotate2(data):
    return nh_rotate_adjacent(data, 2)

def nh_rotate3(data):
    return nh_rotate_adjacent(data, 3)

def nh_rotate4(data):
    return nh_rotate_adjacent(data, 4)

def nh_rotate5(data):
    return nh_rotate_adjacent(data, 5)

def nh_rotate6(data):
    return nh_rotate_adjacent(data, 6)

def nh_rotate7(data):
    return nh_rotate_adjacent(data, 7)

def nh_rotate8(data):
    return nh_rotate_adjacent(data, 8)

def nh_rotate9(data):
    return nh_rotate_adjacent(data, 9)

def nh_rotate10(data):
    return nh_rotate_adjacent(data, 10)

def full_neighbourhood():
    fns = [nh_swap1, nh_swap2,nh_swap3, nh_swap4,nh_swap5, nh_swap6,nh_swap7, nh_swap8,nh_swap9, nh_swap10,
           nh_block1, nh_block2,nh_block3, nh_block4,nh_block5, nh_block6,nh_block7, nh_block8,nh_block9, nh_block10,
           nh_rotate1, nh_rotate2,nh_rotate3, nh_rotate4,nh_rotate5, nh_rotate6,nh_rotate7, nh_rotate8,nh_rotate9, nh_rotate10]
    return fns

def desc_neighbourhoods():
    return [nh_swap10,nh_block10,nh_rotate10,
            nh_swap9,nh_block9,nh_rotate9,
            nh_swap8,nh_block8,nh_rotate8,
            nh_swap7,nh_block7,nh_rotate7,
            nh_swap6,nh_block6,nh_rotate6,
            nh_swap5,nh_block5,nh_rotate5,
            nh_swap4,nh_block4,nh_rotate4,
            nh_swap3,nh_block3,nh_rotate3,
            nh_swap2,nh_block2,nh_rotate2,
            nh_swap1,nh_block1,nh_rotate1]

def desc_neighbourhoods_small():
    return [nh_swap5,nh_block5,nh_rotate5,
            nh_swap4,nh_block4,nh_rotate4,
            nh_swap3,nh_block3,nh_rotate3,
            nh_swap2,nh_block2,nh_rotate2,
            nh_swap1,nh_block1,nh_rotate1]

def neighbourhoods_testing1():
    return [nh_swap1,nh_block1,nh_rotate1]

def neighbourhoods_testing1():
    return [nh_swap1,nh_block1,nh_rotate1,
            nh_swap2,nh_block2,nh_rotate2,
            nh_swap3,nh_block3,nh_rotate3]
        
numbers = []

for i in range(0,5):
    numbers.append(i)
    
shifted = numbers



