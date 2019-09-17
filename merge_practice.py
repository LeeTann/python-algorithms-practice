weight_limit = 50
arrayA = [10, 20, 5, 7, 11]
arrayB = [12, 33, 2, 13, 4]
tempArry = []
def getIndiciesOfItemWeights():
  
  for i in range(0, len(arrayA)):
    tempArry.append(arrayA[i])

    for j in range(0, len(arrayB)):
      tempArry.append(arrayB[j])

print(tempArry) 