for i in range(1,101):
  if i % 3 == 0 and i % 5 == 0:
    print("fizzbuzz")
  elif i % 3 == 0:
    print("fizz")
  elif i % 5 == 0:
    print("buzz")
  else:
    print(i)


    
#Second way to do fizzbuzz 
def fizzbuzz(n):
  #pass

  #while loop
  '''number = 1
  while number < n:
    print(number)
    number = number + 1''' 

  #for loop
  for number in range(1,n):
    if number % 3 == 0 and number % 5 == 0:
      print("fizzbuzz")
    elif number % 3 == 0:
      print("fizz")
    elif number % 5 == 0:
      print("buzz")
    else:
      print(number)

value = 20 
print("Fizzbuzz up to ", value)
fizzbuzz(value)