#Function that returns the largest value 
l = [15, 80, 33, 67, 94, 200, 9]
def findLargest(l):
  #using l for lists is a bad practice  
  largest = l[0]
  for num in l:
    if num > largest:
      largest = num
  return largest 

def findLargest(dataset):
  largeSoFar = dataset[0]
  for item in dataset[1:]:
    if item > largeSoFar:
      largeSoFar = item
  return largeSoFar

def buildRandomList(size, maxvalue):
  #result = [] #empty list
  #for x in range(size):
    #result.append(random.randrange(maxvalue))
  #return result 
  result = [random.randrange(maxvalue) for x in range(size)]  # list comprehension 
  return result 

dataset = buildRandomList(20,30)
#max(dataset)



#Function that returns the frequency of v
'''l = [tweleve, five, seven, eleven]
#def freq(l,v):
  #pass'''
def freq(dataset,v):
  #count = 0
  #for item in dataset:
    #if item == v:
      #count = count+1
  #return count
  return len([x for x in dataset if x == v]) #list comprehension 
#[x for x in dataset] --> makes a copy of the dataset
#len([x for x in dataset if x == 5])