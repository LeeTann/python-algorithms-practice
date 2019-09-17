# n-story building with plenty of eggs
# egg gets broken if thrown off f floor or higher
# doesnt get broken if less than floor f
# n = 20 story building
# f = 6th floor 

builing_floors = n 
egg_floor_limit = f
broken_egg = False

def egg_test(n):
  
  if (you dropped egg from top floor and it doesnt break):
    return "you have an unbreakable egg."

  elif (egg dropped from bottom floor and it breaks):
    return "you have weak eggs"

  else:
    start testings which floor will crack the egg.
    can traverse each floor ground-up or find the middle floor
    
    current_floor = n/2 to find midpoint

    if (egg drop and doesnt break):
      current_floor += 1 to climb the floors until it breaks
    
      if (egg breaks):
       return current_floor -1 and end function

    else:
      current_floor -= 1 to keep going down until it breaks

      if (egg doesnt break):
        return current_floor and end 

0(log n)