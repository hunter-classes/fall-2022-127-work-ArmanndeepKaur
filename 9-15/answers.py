#Chapter 7 Exercise 7 
def is_even(n):
    if n % 2 == 0:
        result = True
    else:
        result = False
    
    return result

print(is_even(8))
print(is_even(13))
print(is_even(100))


#Chapter 7 Exercise 8
def is_odd(n):
    if n % 2 != 0:
        result = True
    else:
        result = False
        
    return result

print(is_odd(9))
print(is_odd(127))
print(is_odd(20))


#Chapter 7 Exercise 10
#Chapter 7 Exercise 11






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