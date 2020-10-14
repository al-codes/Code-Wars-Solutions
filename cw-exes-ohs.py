def xo(xostring):
    """Checks if string has equal amount of x's and o's."""

    olist = []
    xlist = []
  
    for letter in xostring.lower():
        if letter == 'o':
            olist.append(letter)
    
        if letter == 'x':
            xlist.append(letter)
      
    if len(olist) == len(xlist):
        return True
    
    elif len(olist) != len(xlist):
        return False

test1 = print(xo('ooxx'))
# should return True

test2 = print(xo('xooxx')) 
# should return False 
