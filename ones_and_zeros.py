# Given an array of ones and zeroes, convert the equivalent binary value to an integer.

# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

def binary_array_to_number(arr):
  # your code
  output = []
  
  for i in arr:
    output.append(str(i)) # convert to string
    print(output)
    
  output = "".join(output) # join the string
  print("string output", output)
  # int(output, 2) for binary code
  return int(output, 2)

print(binary_array_to_number([1,1,0,1,0]))