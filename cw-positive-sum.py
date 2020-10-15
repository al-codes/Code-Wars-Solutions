def positive_sum(array):
    """Returns the sum of all positive nums in an array"""

    positive_nums = []
    
    for dig in array:
        if dig > 0:
              positive_nums.append(dig)
      
    return sum(positive_nums)

test = print(positive_sum([4,5,2,-2,-6,-12,-4,1]))
# should return 12
            
