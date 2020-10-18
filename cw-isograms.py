def is_isogram(string):
    """Returns true is string is an isogram -  no repeating letters"""
    
    checked_letters = []
    
    for x in string.lower():
        if x in checked_letters:
            return False
        checked_letters.append(x)
        
    return True

test1 = print(is_isogram("Dermatoglyphics" ))
# prints true
test2 = print(is_isogram("aba" ))
# prints false
test3 = print(is_isogram("moOse" ))
# prints false -- ignores letter case
