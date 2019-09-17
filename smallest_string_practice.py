# function takes two strings and return smallest
# if strings are == return any string


def smallest_function(string1, string2):
  smallest_letter = ""

  for i in string1:
    print(i)
    for j in string2:
      print(j)

      if i > j:
        smallest_letter = i
      else:
        smallest_letter = j
    
    return smallest_letter

print(smallest_function("mom", "dad"))