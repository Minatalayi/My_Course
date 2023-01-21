import turtle as t

t.shape("turtle")
t.width(2)
t.color("black")
t.bgcolor("green")
t.speed(3)
t.penup()
t.pendown()

i=0
j=0
side=0

while i < 10:
    
    degree = ( ((i+1)*180) / (i+3) )
    t.left(180 - (degree / 2))
    side += 106

    while j <= i+2:
        t.fd( side / (i+3) )
        t.lt(180 - degree)
        j += 1

    t.penup()
    t.right(180 - degree)
    t.right(degree / 2)
    t.forward(17)
    t.pendown()
    j=0
    i+=1       