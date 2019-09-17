# Create a function that finds the integral of the expression passed.

# In order to find the integral all you need to do is add one to the exponent (the second number), and divide the coefficient by that new number (the first number).

# In 3x^2, for example, the integral would be 1x^3 (we added 1 to the exponent, and divided the coefficient by that new number).

def integrate(coefficient, exponent):
    # write your code here
    exponent = exponent + 1
    coefficient = coefficient // exponent
    exponent = str(exponent)
    coefficent = str(coefficient)
    
    return coefficent + "x^" + exponent
print(integrate(90,2))