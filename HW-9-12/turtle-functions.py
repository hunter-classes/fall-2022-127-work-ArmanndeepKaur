import turtle 

#Draw a Hexagon with the same parameters as square and triangle 
def hexagon(t, x, y, w, color, sidelen):
   t.penup()
   t.goto(x,y)
   t.width(w)
   t.color(color)
   t.pendown()
    
   for i in range(6):
     t.forward(sidelen)
     t.left(60)

wn = turtle.Screen()
ann = turtle.Turtle()
hexagon(ann, 0, 0, 2, "#f37736", 100)



#Draw a ngon with parameters(t, numsides, x, y, color, width, sideln)
def ngon(t, numsides, x, y, color, width, sidelen):
    t.penup()
    t.goto(x,y)
    t.width(width)
    t.color(color)
    t.pendown()
    
    # for i in range(9):
    #     t.forward(sidelen)
    #     t.left(40)

#Use of numsides
    for i in range(numsides):
      t.forward(sidelen)
      t.right(360/numsides)

anna = turtle.Turtle()
ngon(anna, 5, 23, 23, "blue", 3, 80)


wn.mainloop()
