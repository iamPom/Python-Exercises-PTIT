
# a list contains both even and odd numbers. 
seq = [0, 1, 2, 3, 5, 8, 13]
  
# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))
  
# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))