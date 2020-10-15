def invert(lst):
    """Takes list of nums and returns a list of the inverses of each num"""

    inv_nums = []
    
    for x in lst:
        inv = x * -1
        inv_nums.append(inv)
    
    return inv_nums

test1 = print(invert([1,2,3,4,5]))
# should print [-1,-2,-3,-4,-5]
test2 = print(invert([1,-2,3,-4,5]))
# should print [-1,2,-3,4,-5]
test3 = print(invert([]))
# should print []