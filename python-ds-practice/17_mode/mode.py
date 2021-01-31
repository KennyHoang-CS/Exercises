def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    counter = {}
    
    # Count the number for each occurrence. 
    for n in nums:
        counter[n] = counter.get(n, 0) + 1 

    # Find the value with the highest counts. 
    findMax = max(counter.values())
    
    # Find the key with the highest counts. 
    for (key, freq) in counter.items():
        if freq == findMax:
            return key 


print(mode([1, 2, 1]))
print(mode([2, 2, 3, 3, 2]))

    
