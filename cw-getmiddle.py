def get_middle(s):
    """Takes in a string and returns middle letter for odd length or two middle letters for even length."""
    
    if(len(s) % 2 == 0):
        return "" + s[(int(len(s) / 2) - 1 )] + s[(int(len(s) / 2))]
    
    else:
        return s[(int(len(s)/2))]

test1 = print(get_middle("test")) 
# should return "es"

test2 = print(get_middle("testing")) 
# should return "t"

test3 = print(get_middle("middle"))
# should return "dd"

test4 = print(get_middle("A"))
# should return "A"