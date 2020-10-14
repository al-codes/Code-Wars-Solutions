def summation(num):
    """Returns the summation of every number from 1 to num."""
    num_to_add = []
    
    for x in range(1, num + 1):
        num_to_add.append(x)
        
    return sum(num_to_add)

test = print(summation(10))
# should return [1 + 2 ... + 9 + 10] == 55