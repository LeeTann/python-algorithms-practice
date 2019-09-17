# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

def filter_list(l):
  'return a new list with the strings filtered out'

  new_list = []

  for char in l:
    if type(char) == int:
      new_list.append(char)

  return new_list
