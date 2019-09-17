# array can be empty - return 0
# max array length is 1000. 
# array value is between 0 and 1000
# count each pair only once

def duplicate(arr):

  if len(arr) <= 1: # 0(1)
    return 0

  count_arr = [0] * (max(arr) + 1) # 0(n)

  for num in arr: # 0(n)
    count_arr[num] += 1 # 0(1)

  duplicate_count = 0
  for num in count_arr: # 0(max in n) or 0(m)
    duplicate_count += num // 2 # 0(1)

  return duplicate_count

print(duplicate([1, 1, 5, 6, 2, 2]))
# runtime is 0(n) + 0(m)

def duplicate_with_dict(arr2):

  if len(arr2) <=1:
    return 0

  counter_dict = {}

  for num in arr2:
    if num not in counter_dict:
      counter_dict[num] = 1
    else:
      counter_dict[num] += 1
  
  duplicate_counter = 0
  for value in counter_dict.values():
    duplicate_counter += value // 2

  return duplicate_counter