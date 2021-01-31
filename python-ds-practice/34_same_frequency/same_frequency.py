def makeCountDict(num):
    """ Make a dictionary by counting the frequencies of each digit. """
    count = {}
    for n in num:
        count[n] = count.get(n, 0) + 1
    return count

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    return makeCountDict(str(num1)) == makeCountDict(str(num2))
    
    

print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))

