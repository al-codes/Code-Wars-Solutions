def square_sum(numbers):
  
  squared_sum = sum([(num ** 2) for num in numbers])
  
  return squared_sum


test = print(square_sum([2,4,8]))
# prints 84
