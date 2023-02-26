import turtle
tao = turtle.Pen()
tao.shape('turtle')
tao.color('Green')
for i in range(8):
    tao.left(45)
    tao.forward(50)
tao.penup()
tao.goto(100,-200)
tao.pendown()
for i in range(80):
    tao.backward(200)
    tao.right(125)
turtle.done()

