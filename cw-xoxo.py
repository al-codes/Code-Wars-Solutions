# Code Wars - X's and O's
# Write a function that checks if equal x's and o's in a string

def XO(str):
    """Returns true if there are equal amount of x's and o's in string"""

    o_list = []
    x_list = []
  

    for letter in str.lower():
        if letter == 'o':
            o_list.append(letter)

        if letter == 'x':
            x_list.append(letter)
      
    if len(o_list) == len(x_list):
        return True
    
    else:
        return False

test = XO('xxxxooo') # Returns False
test2 = XO('xxxooo') # Returns True
