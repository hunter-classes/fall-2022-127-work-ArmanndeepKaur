#Function that returns the largest value 
l = [15, 80, 33, 67, 94, 200, 9]
def findLargest(l):
  largest = l[0]
  for num in l:
    if num > largest:
      largest = num
  return largest 


#Function that returns the frequency of v
l = [tweleve, five, seven, eleven]
def freq(l,v):
  ...