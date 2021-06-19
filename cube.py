import turtle as td
from turtle import Turtle as ttl
z = 0.7
wn = td.Screen()
wn.tracer(0)

pen = ttl()
pen.width(7)
pen.speed(10)
pen.ht()

def xdraw(direction,leng):
	pen.pd()
	if direction > 0:
		pen.seth(180)
	else:
		pen.seth(0)
	pen.fd(leng)
	pen.pu()
	wn.update()
	

def ydraw(direction,leng):
	pen.pd()
	if direction > 0:
		pen.seth(270)
	else:
		pen.seth(90)
	pen.fd(leng)
	pen.pu()
	wn.update()
	

def zdraw(direction,leng):
	pen.pd()
	if direction < 1:
		pen.seth(45)
	else:
		pen.seth(225)
	pen.fd(leng*z*1.1)
	pen.pu()
	wn.update()



blef = pen.pos()

xdraw(0,77)
brit= pen.pos()

ydraw(0,77)
trit = pen.pos()

xdraw(1,77)
tleft= pen.pos()

ydraw(1,77)

pen.goto(tleft)
zdraw(0,77)
xdraw(0,77)
ydraw(1,77)
pen.goto(trit)
zdraw(0,77)

pen.goto(brit)
zdraw(0,77)

wn.mainloop()