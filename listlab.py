#Chapter 10 Exercise 10 --> Count how many words in a list have length 5 
listA = ["Replit", "Lab", "CS", "Tablet", "seven"]
count = 0
for words in listA:
  if len(words) == 5:
    count = count+1
print(count)  


#Chapter 10 Exercise 11 --> Sum all the elements in a list up to but not including the first even number 
'''nums = [1,2,3,4,5,6,7,8]
def adding_num(x):
  sum = 0
  for elements in nums:
    if elements % 2 == 0:
      sum = sum + 1
    return sum'''

def up_to_even(l):
    result = []
    i = 0
    while l[i] % 2 != 0:
        result.append(l[i])
        i = i+1
    return result


#Chapter 10 Exercise 12 --> Count how many words occur in a list up to and including the first occurance of the word 'sam'
'''randoms ={"Anna", 92.3, "True", "Sam", 92.3, 76, 4, False, "hello"}
print(randoms.count('sam'))
del randoms[4:]
print(randoms)''' 

def up_to_sam(l):
    result = []
    i = 0
    while l[i] != "sam":
        result.append(l[i])
        i = i+1
    return " ".join(result)

#Most of my own codes for the lab were wrong or were not written as functions, therefore, I deleted them (learned where I made mistakes and how I can improve) and replaced them with codes from the github (because I will look back at these)

#Function that finds the smallest value 
def find_smallest(thelist):
    small_so_far = thelist[0]
    for item in thelist[1:]:
        if item < small_so_far:
            small_so_far = item
    return small_so_far
  

#Function that returns a new list with all the odd items from the orginial list 
def odd_items(l):
  result = []
  for items in l:
    if items % 2 == 1:
        result.append(items)
  return result 


#Function that returns a string with captalized words 
def capitalization():
  result_list = []
    for word in s.split():
        result_list = result_list + [word.capitalize()]
    result = " ".join(result_list) #learn how and why to use .join
    return result


#Function that returns a string with 5+ words uppercase 
def long_5_cap(s):
    result_list = []
    for word in s.split():
        if len(word) > 5:
            result_list = result_list + [word.upper()]
        else:
            result_list = result_list + [word]
    result = " ".join(result_list)
    return result


#Function that returns each item squared 
def square_list(l):
  result = []
  for item in l:
    #result = item**2
    result.append(item*item)
  return result


#Function that returns corresponding values and add the lists together 
ef combine_sum(l1,l2):
    result = []
    if len(l1) < len(l2):
        shorter = len(l1)
    else:
        shorter = len(l2)
    for i in range(shorter):
        result.append(l1[i] + l2[i])
    if len(l1) > shorter:
        result = result + l1[i:]
    else:
        result = result + l2[i:]
    return result








