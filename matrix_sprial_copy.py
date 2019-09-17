# Given a 2D array (matrix) inputMatrix of integers, 
# create a function spiralCopy that copies inputMatrix’s values into a 1D array in a clockwise spiral order. 
# Your function then should return that array.

# Examples:

# input:  inputMatrix  = [
#                         [1, 2, 3, 4, 5],
#                         [6, 7, 8, 9, 10],
#                         [11, 12, 13, 14, 15],
#                         [16, 17, 18, 19, 20]
#                        ]

# output: [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
# Analyze the time and space complexities of your solution.

# see how many sub array there are. 
# loop thru the first sub array and add it to output 

def spiralCopy(inputMatrix):
    numRows = len(inputMatrix)
    numCols = len(inputMatrix[0])
    
    # keep track of our location
    topRow = 0
    bottomRow = numRows - 1
    leftCol = 0
    rightCol = numCols - 1

    output = []

    # iterate through the entire matrix
    while topRow <= bottomRow and leftCol <= rightCol:

        # iterate through the top row from left to right
        for i in range(leftCol, rightCol + 1):
            output.append(inputMatrix[topRow][i])
        topRow += 1
        print(topRow)

        # iterate along the right column from top to bottom
        for i in range(topRow, bottomRow + 1):
            output.append(inputMatrix[i][rightCol])
        rightCol -= 1
        print(rightCol)

        if topRow <= bottomRow:
            # iterate along the bottom row from right to left
            for i in reversed(range(leftCol, rightCol + 1)):
                output.append(inputMatrix[bottomRow][i])
            bottomRow -= 1
            print(bottomRow)
        
        if leftCol <= rightCol:
            # iterate along the left column from bottom to top
            for i in reversed(range(topRow, bottomRow + 1)):
                output.append(inputMatrix[i][leftCol])
            leftCol += 1
            print(leftCol)


    return output

print(spiralCopy(
  [[1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20]]
))  # should print [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
