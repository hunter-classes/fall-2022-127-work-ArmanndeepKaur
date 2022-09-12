import turtle 

#Draw a Hexagon with the same parameters as square and triangle 
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



#Draw a ngon with parameters(t, numsides, x, y, color, width, sideln)
def ngon(t, numsides, x, y, color, width, sidelen):
    t.penup()
    t.goto(23,23)
    t.width(3)
    t.color("blue")
    t.pendown()
    
    for i in range(9):
        t.forward(sidelen)
        t.left(40)

anna = turtle.Turtle()
ngon(anna, 9, 23, 23, "blue", 3, 50)


wn.mainloop()
