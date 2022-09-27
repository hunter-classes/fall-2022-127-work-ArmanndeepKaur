
#Funtion 1 
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




#Function 2
def piglatinify(word):
  first = word[0]
  if first in 'aeiou':
    result = word + 'yay'
  else:
    #move the first letter to end and add 'ay'
    result = word[1:]+first+'ay'

  return result


#Testing 
test_word = "hello"
result = piglatinify(test_word)
print(test_word," -> ",result)

test_word = "able"
result = piglatinify(test_word)
print(test_word," -> ",result)

test_word = "Cable"
result = piglatinify(test_word)
print(test_word," -> ",result)

test_word = "Able."
result = piglatinify(test_word)
print(test_word," -> ",result)

test_word = "cable."
result = piglatinify(test_word)
print(test_word," -> ",result)






 #Longer way to convert a word into piglatin 
'''def piglatin(word):
  """
  input: a string representing a word 
  returns: a new string with the word converted to piglatin 
  """ 
      #Converting the word into piglatin
  consonent_first = word[1].upper() + word[2:7] + word[0] + "ay"
  result = consonent_first
  return result
      #Testing piglatin
result = piglatin("morning")
print("morning --> ", result)'''
