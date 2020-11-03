def odd_or_even(arr):
    """Returns whether the sum of a given array of numbers is odd or even."""

    if sum(arr) % 2 == 0:
        return "even"
    else:
        return "odd"


test1 = odd_or_even(["1, 2, 3"])
# prints "even" ==> 1 + 2 + 3 = 6

test2 = odd_or_even(["2, 3, 4"])
# prints "odd" ==> 2 + 3 + 4 = 9 