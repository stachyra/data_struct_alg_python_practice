def remove_duplicates(x, nullval):
    """
    Given a sorted 1-D data structure (either a list or numpy array), remove
    duplicate entries and reorder unique entries to the front, without using
    any temporary variables outside the array to hold data from within the
    array.  Write a substitute null value to the rear, unneeded portions
    of the array, and return the length of the deduplicated data.
    """

    # Edge cases:
    #
    #   1.) array has no duplicates because it has < 2 elements
    #   2.) array has >= 2 elements but has no duplicates
    #   3.) array has >= 2 elements and just one value (all duplicates)

    # Index to which we are currently overwriting
    i = 0
    # Index to test
    for j in range(1,len(x)):
        if x[i] != x[j]:
            i += 1
            x[i] = x[j]

    # Write null to unused portion of data structure
    for j in range(i+1,len(x)):
        x[j] = nullval

    return i+1

def shift_zeros(x):
    """
    Given a sorted 1-D data structure (either a list or numpy array)
    containing some zeros, move all zeros to the back of the array and
    rewrite non-zero values, preserving their original ordering, at the
    front, without using any temporary variables outside the array to
    hold data from within the array, and return the length of the non-zero
    portion of the array.
    """

    # Edge cases:
    # 
    #   1.) input array contains no elements,
    #   2.) input array contains 1 element, which is zero
    #   3.) input array contains 1 element, which is non-zero
    #   4.) input array contains no zeros
    #   5.) input array contains all zeros
    #
    # Concepts to be represented by variables:
    # 
    #   1.) index of cell currently being checked for zeroes
    #   2.) index of cell where a non-zero entry is currently being rewritten

    i = 0
    for j in range(len(x)):
        if x[j] == 0:
            continue
        else:
            x[i] = x[j]
            i += 1

    for j in range(i, len(x)):
        x[j] = 0

    return i
