#Chapter 7 Exercise 7 
def is_even(n):
  '''
  n: an integer value 
  returns: true if n is even, false otherwise
  '''
  #pass = passing to the next statement; a placeholder 
  #None = it means nothing, it doesn't exist 
  
  if n % 2 == 0:
        return True #result = True
  else:
        return False #result = False 
        #return result
print("Even Tests")
result = is_even(10)
print("Result for 10 is:", result)
result = is_even(11)
print("Result for 11 is:", result)
# print(is_even(8))
# print(is_even(13))
# print(is_even(100))


#Chapter 7 Exercise 8
def is_odd(n):
  return not(is_even(n))

print("Odd Tests")
result = is_odd(10)
print("Result for 10 is:", result)
result = is_odd(11)
print("Result for 11 is:", result)
#     if n % 2 != 0:
#         result = True
#     else:
#         result = False  
#     return result
# print(is_odd(9))
# print(is_odd(127))
# print(is_odd(20))


#Chapter 7 Exercise 10
def is_rightangled(a, b, c):
  '''
  c is the longest side
  '''
  return a*a + b*b == c*c


#Chapter 7 Exercise 11
def is_rightangled2(a, b, c):
  '''
  Any order for sides 
  '''
  return is_rightangled2(a, b, c) or \
          is_rightangled2(b, c, a) or \ 
          is_rightangled2(a, c, b)

print(is_rightangled(5,3,4))
print(is_rightangled2(5,3,4))



#CodingBat Strings-1

#hello_name Hello Bob!
def hello_name(name):
  return "Hello " + name + "!"
print(hello_name("Bob"))


#make_out_word <<word>>
def make_out_word(put, word):
  return out[:2] + word + out[2:]
print(make_out_word("YAY"))


#first_two
def first_two(str):
  return str[:2]
print(first_two("Hello"))