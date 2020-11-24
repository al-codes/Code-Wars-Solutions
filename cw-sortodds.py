def sort_array(source_array):
    """Returns array with only odd numbers sorted in ascending order."""
    
    odds = []
    other_nums = 0

    for num in source_array: 
        if num % 2 != 0:
            odds.append(num)
    odds.sort()

   
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = odds[other_nums]
            other_nums += 1
            
    return source_array