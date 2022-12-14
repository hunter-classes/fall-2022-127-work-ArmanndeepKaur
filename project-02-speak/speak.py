#Setup
text = open('input.txt')
input = text.read()

print("ORIGINAL")
print(input)
print()

myDict = {"I":"maen",
          "excited":"wonden", 
          "for":"about",
          "friend":"matey", 
          "birthday":"janamwon",
          "days":"deen",
          "gift":"treasure",
          "good":"cool",
          "happy":"joy",
          "don't":"nowwe",
          "her":"keiv"}

#Basic 
for words in myDict:
  input = input.replace(words, myDict[words])
print("BASIC/TRANSLATION")
print(input)
print()

#Extra --> Punctuation (handling uppercase/lowercase)
print("EXTRA/FINAL")
input = ('. '.join([letters.lstrip().capitalize() for letters in input.split('.')]))
print(input)

'''for letters in input.split('. '):
  result = []
  result.append(letters.lstrip().capitalize())
  result = " ".join(result)
  print(result, end = '. ')'''