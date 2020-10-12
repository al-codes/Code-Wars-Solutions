def filter_list(stringnum_list):
    """Takes a list of non-negative integers and strings and returns a list with the strings filtered out"""
    
    integers = []
    
    for item in stringnum_list:
        if type(item) == int:
            integers.append(item)
            
    return integers

test1 = print(filter_list([1,2,'a','b']))
# prints [1,2]
test2 = print(filter_list([1,'a','b',0,15]))
# prints [1,0,15]
test3 = print(filter_list([1,2,'aasf','1','123',123]))
# prints [1,2,123]