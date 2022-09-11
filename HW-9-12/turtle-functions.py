#Draw a Hexagon with the same parameters as square and triangle 

import turtle 

def hexagon(t, x, y, w, color, sidelen):

  t.penup()
  t.goto(0,0)
  t.width(2)
  t.color("#f37736")
  t.pendown()
    
  for i in range(6):
    t.forward(sidelen)
    t.left(60)

wn = turtle.Screen()
ann = turtle.Turtle()
hexagon(ann, 0, 0, 2, "#f37736", 100)