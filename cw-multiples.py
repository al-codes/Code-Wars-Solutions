def multiple_adder(number):
    """Returns the sum of all the multiples of 3 or 5 below the number passed in."""

    multiples_added = 0
    
    if number > 0:
        for digit in range(0, number):
            if digit % 3 == 0 or digit % 5 == 0:
                multiples_added += digit
                
        return multiples_added
    
    else:
        return 0

test = print(multiple_adder(10))
# 23
test = print(multiple_adder(-10))
# 0 -- problems says if negative number, function should return 0

