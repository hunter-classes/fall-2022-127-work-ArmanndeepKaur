def bondify(name):
    """
    input: a string in the form "first last"
    returns: a string in the form "Last, First Last"
    """
    result = ""
    
  # isolate, uppercase and add first init to result
    last = name[6]
    last = last.upper()
    last = result + last

  # find the last name (after space), cap it and add to result
    location = name.find(' ')
    last = name[location+1:].capitalize()
    
  # full name 
    first = name[0:]
    first = first[0].upper() + first[1:5] + " " + first[6].upper() + first[7:10]
    first = result + first
    
    result = result + last + "," + " " + first
    return result
    
# Test bondify
result = bondify("james bond")
print("james bond --> ", result) 