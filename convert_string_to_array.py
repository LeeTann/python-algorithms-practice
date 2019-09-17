# Write a function to split a string and convert it into an array of words. For example:

# "Robin Singh" ==> ["Robin", "Singh"]

# "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]

def string_to_array(s):
    # your code here
    array = list(s.split(" "))
    return array


print(string_to_array("Robin Singh"))