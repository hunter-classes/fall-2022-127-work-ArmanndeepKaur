#I recieved assistance from Irene, Jose, and Kai Min

import random 

#Extra 1 --> writing a stoty in a file and reading from it 
file_text = open('story.txt')
s = file_text.read()

verbs = ['running', 'crying', 'falling', 'sleeping']
nouns = ['park', 'book', 'bus', 'mountain', 'restaurant']
#Extra 2 --> unique replacement 
names = ['Zoe', 'Ann', 'Lea', 'Isa', 'Taj']

#Irene helped me with this part because my code was not printing out all three things (noun, name, verb) at the same time
def madlibs(s):
  story = []
  for word in s.split():
    story = story + [word.replace("<name>", random.choice(names)).replace("<verb>", random.choice(verbs))
                   .replace("<noun>", random.choice(nouns))]
    result = " ".join(story)
    return result 

print(madlibs(s))

