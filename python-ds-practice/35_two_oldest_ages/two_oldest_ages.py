def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)
    """
    distinctAges = set(ages)

    # Get the first highest age. 
    age1 = max(distinctAges)

    # Remove the first highest age from the set. 
    distinctAges.remove(age1)

    # Get the second highest age.
    age2 = max(distinctAges)

    # Return the two highest ages as a tuple. 
    return (age2, age1)


print(two_oldest_ages([1, 2, 10, 8]))
print(two_oldest_ages([6, 1, 9, 10, 4]))
print(two_oldest_ages([1, 5, 5, 2]))