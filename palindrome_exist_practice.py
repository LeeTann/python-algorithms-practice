# validate input
# be able to process num 1 digit at a time
# detect a palindrome

def palindrome(num):

  if num < 0 or type(num) != int:
    return "Not valid"

  str_num = str(num)

  if len(str_num) <= 1:
    return False

  i = 0
  while i < len(str_num) - 2:
    # check that current char == next char
    #check double digit palindrome
    if str_num[i] == str_num[i+1]:
      return True
    
    # check triple digit palindrom
    if i < len(str_num) - 3 and str_num[i] == str_num[i+2]:
      return True
    i += 1

  return False