def count_bits(n):
    """Takes in an integer and returns the number of bits that are equal to one in the binary representation of that number."""
    
    bits = 0
    
    n = bin(n)
    
    for num in str(n):
        if num == "1":
            bits += 1

    return bits

test = print(count_bits(1234))
# binary of 1234 is 10011010010, so the function should return 5 