def descending_order(num):
    """Takes in a non-negative integer and returns digits in descending order."""

    sorted_num = sorted(str(num), reverse=True)
    
    joined_num = "".join(sorted_num)
    
    return int(joined_num)

test1 = print(descending_order(42145))
# should print 54421

test2 = print(descending_order(123456789))
# should print 987654321