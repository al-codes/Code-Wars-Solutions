def disemvowel(string):
    """Returns a string without vowels."""

    for i in "aeiouAEIOU":
        string = string.replace(i,"")
    
    return string

test = print(disemvowel('this is a test'))
# returns 'ths s  tst'