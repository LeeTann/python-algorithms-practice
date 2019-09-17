# Given a package with a weight limit limit and an array arr of item weights, 
# implement a function getIndicesOfItemWeights that finds two items whose sum of 
# weights equals the weight limit limit. Your function should return a pair [i, j]
# of the indices of the item weights, ordered such that i > j. 
# If such a pair doesn’t exist, return an empty array.

# Analyze the time and space complexities of your solution.

# Example:

# JavaScript:

# input: arr = [4, 6, 10, 15, 16]
#        limit = 21
# output: [3, 1]   // since these are the indices of 
#                  // weights 6 and 15 whose sum equals 21

# Understand
# - create a function called getIndicesOfItemWeights
# - the array called arr
# - limit called limit
# - output an array of the two valid indicies
# - loupe through the array, 
# - if number is greater than limit - discard.
# - add i + j, see if equal limit. if so, return indicies.
# - if not continue 
# - return empty array if pair doesnt exist

# if the sum of two number equals the weight limit
# return the index of those two number
# since we are giving the weight limit and individual numbers, we know
# that weight limit - individual number = missing value.

# use a dict to store the item weights along with their 'complement'
output = {}

def getIndicesOfItemWeights(arr, limit): 

  # loop thru the array and find the missing value
  for i in range(len(arr)):
    weight = arr[i]
    missing_value = limit - weight
    print("missing value:", missing_value)

    # if missing value is in the ouptut dict
    if missing_value in output:
      # then we are done. return the index and missing value index
      return [i, output[missing_value]]
    else:
      # otherwise, store the weight with its index in in output
      output[weight] = i
      print("output weight: ", output[weight])
  return output

print(getIndicesOfItemWeights([4, 6, 10, 15, 16], 21))