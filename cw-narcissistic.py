def narcissistic( value ):
    """Returns True if value is a Narcissistic number in base 10"""
    
    value_nums = []
    value_length = int(len(str(value)))
    powered_nums = []
    
    for dig in str(value):
        value_nums.append(dig)

    for num in value_nums:
        pow_nums = int(num) ** value_length
        powered_nums.append(pow_nums)
    
    if sum(powered_nums) == int(value):
        return True
    else:
        return False

    test1 = print(narcissistic(153))
    # prints True  ==>1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

    test2 = print(narcissistic(1652))
    # prints False  ==>1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938