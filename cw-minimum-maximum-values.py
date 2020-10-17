def minimum(arr):
   """Returns minimum and maximum values of a given list."""
   
   minimum_num = []
   
   for dig in arr:
       minimum_num.append(dig)
    

    return minimum_num.sort()
        
def maximum(arr):
    
    maximum_num = []
    
    for dig in arr:
        maximum_num.append(dig)
        maximum_num.sort()

    return maximum_num[-1]

test1 = print(maximun([4,6,2,1,9,63,-134,566])) 
# returns 566
test2 = print(minimun([-52, 56, 30, 29, -54, 0, -110]))
# returns -110
test3 = print(maximun([5]))
# returns 5
test4 = print(minimun([42, 54, 65, 87, 0])) 
# returns 0