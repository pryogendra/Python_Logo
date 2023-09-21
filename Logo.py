import turtle as t

s = t.Screen()
s.bgcolor('gray')

#t.speed(0)
t.pensize(8)
t.penup()
t.left(90)
t.forward(250)
t.left(90)
t.forward(400)
t.left(180)
t.pendown()

t.pencolor("orange")
t.pensize(4)
t.forward(124) #line
t.backward(117)
t.pencolor("dark blue")
t.pensize(8)
t.penup()
t.left(90)
t.forward(10)
t.pendown()
t.forward(50) #t
t.backward(7)
t.left(90)
t.forward(7)
t.backward(14)
t.penup()
t.backward(10)
t.pendown()
t.backward(100)
t.penup()
t.forward(90)
t.left(70)
t.forward(20)
t.pendown()
for i in range(30):
	t.backward(1)
	t.right(5)

def ll():
    for i in range(30):
        t.forward(1)
        t.left(5)
ll() #c
t.left(19)
t.forward(15)
ll()
t.left(-60)
t.penup()
t.forward(15)
t.pendown()
t.left(300) #s
for i in range(3):
    t.backward(1.18)
    t.right(8)
for i in range(30):
    t.forward(1.18)
    t.left(8)
t.forward(7.95)
for i in range(30):
    t.forward(1.18)
    t.right(8)
t.penup()
t.forward(6)
t.left(90)
t.forward(35)
t.pendown()
t.left(100)
ll() #c
t.left(19)
t.forward(15)
ll()


t.penup()
t.right(155)
t.forward(250)
t.left(90)
t.pendown()

t.speed(10)   #python logo design
t.pensize(5)
t.pencolor("white")

def s_curve():
    for i in range(90):
        t.left(1)
        t.forward(1)

def r_curve():
    for i in range(90):
        t.right(1)
        t.forward(1)

def l_curve():
    s_curve()
    t.forward(80)
    s_curve()

def l_curve1():
    s_curve()
    t.forward(90)
    s_curve()

def half():
    t.forward(50)
    s_curve()
    t.forward(90)
    l_curve()
    t.forward(40)
    t.left(90)
    t.forward(80)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(120)
    l_curve1()
    t.forward(30)
    t.left(90)
    t.forward(50)
    r_curve()
    t.forward(40)
    t.end_fill()

def get_pos():
    t.penup()
    t.forward(20)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.pendown()

def eye():
    t.penup()
    t.right(90)
    t.forward(160)
    t.left(90)
    t.forward(70)
    t.pencolor("black")
    t.dot(35)

def sec_dot():
    t.left(90)
    t.penup()
    t.forward(310)
    t.left(90)
    t.forward(120)
    t.pendown()

    t.dot(35)


t.fillcolor("#306998")
t.begin_fill()
half()
t.end_fill()
get_pos()
t.fillcolor("#FFD43B")
t.begin_fill()
half()
t.end_fill()

eye()
sec_dot()

t.penup()
t.backward(380)
t.right(90)
t.forward(90)
t.left(90)

t.write("Created By :- ",align='left',font=('Arial',20))
t.pencolor('red')
t.forward(50)
t.pendown()
t.pensize(8)
def y():
        t.right(60) #Y
        t.forward(20)
        t.right(180)
        t.backward(20)
        t.right(60)
        t.forward(40)
        t.backward(40)
        t.left(210)
        t.forward(40)
y()
t.penup()
t.left(90)
t.forward(30)
t.right(90)
t.forward(10)
t.forward(20)
t.backward(60)
t.forward(15)
t.pendown()
def u():
	for i in range(45):
		t.forward(1)
		t.left(4)
def u_back():
	for i in range(45):
		t.forward(1)
		t.right(4)
def half_u():
	for i in range(45):
		t.forward(0.70)
		t.left(2)
def half_u_back():
        for i in range(45):
                t.forward(0.70)
                t.right(2)
u()#O
t.forward(45)
u()
t.forward(45)
t.penup()
t.left(90)
t.forward(40)
t.right(90)
t.pendown()
u() #G
t.forward(20)
t.left(90)
t.forward(10)
t.penup()
t.backward(25)
t.left(90)
t.forward(13)
u_back()
t.left(90)
t.forward(15)
t.right(90)
t.pendown()
t.forward(40)
u_back()
t.left(90)
t.penup()
t.forward(10)
t.left(90)
t.forward(-5)
t.pendown()
t.forward(20) #E
t.right(90)
t.forward(25)
t.backward(25)
t.right(90)
t.forward(37)
t.left(90)
t.forward(15)
t.backward(15)
t.right(90)
t.forward(37)
t.left(90)
t.forward(25)
t.penup()
t.forward(10)
t.pendown()
def n():
        t.left(90) #N
        t.forward(75)
        t.right(160)
        t.forward(80)
        t.left(160)
        t.forward(75)
n()
t.penup()
t.right(90)
t.forward(10)
t.right(90)
t.pendown()
def d():
        t.forward(75) #D
        t.left(90)
        half_u()
        t.forward(35)
        half_u()
d()
t.penup() 
t.backward(30)
t.pendown()
t.left(90)
def r():
        t.forward(75) #R
        t.backward(75)
        t.left(90)
        half_u_back()
        half_u_back()
        t.left(125)
        t.forward(43)
r()
t.penup()
t.left(55)
t.forward(10)
t.pendown()
def a(): #A
        t.left(78)
        t.forward(75)
        t.right(155)
        t.forward(75)
        t.backward(35)
        t.right(100)
        t.forward(15)
a()
t.penup()
t.backward(60)
t.left(90)
t.pendown()
t.right(3)
t.forward(37) #P
t.backward(75)
t.left(90)
half_u_back()
half_u_back()
t.penup()
t.backward(30)
t.left(90)
t.backward(40)
t.pendown()
r() #R
t.penup()
t.left(55)
t.forward(10)
t.pendown()
a() #A

def s():
        for i in range(10):
            t.backward(0.85)
            t.right(3)
        for i in range(90):
            t.forward(0.85)
            t.left(3)
        t.forward(20)
        for i in range(90):
            t.forward(0.85)
            t.right(3)
t.penup()
t.backward(35)
t.left(90)
t.right(3)
t.forward(15)
t.pendown()
s() #S
t.penup()
t.left(45)
t.forward(50)
t.right(-75)
t.pendown()
a() #A
t.penup()
t.backward(35)
t.left(90)
t.pendown()
t.right(3)
t.backward(37)
d() #D
t.penup()
t.backward(60)

t.left(90)
t.forward(55)
t.pendown()
t.pencolor('green')
s() #S
t.penup()
t.backward(25)
t.left(135)
t.pendown()
t.right(105)
t.forward(50) #U
for a in range(60):
	t.forward(1)
	t.left(3)
t.forward(50)

t.penup()
t.right(90)
t.forward(10)
t.pendown()
t.forward(25) #F
t.backward(25)
t.right(90)
t.forward(30)
t.left(90)
t.forward(20)
t.backward(20)
t.right(90)
t.forward(40)

t.penup()
t.left(90)
t.forward(35)
t.left(90)
t.pendown()

t.forward(70) #I
t.penup()
t.right(90)
t.forward(10)
t.pendown()
y() #Y

t.left(90)
t.penup()
t.forward(20)
t.pendown()
t.left(78)#A
t.forward(75)
t.right(155)
t.forward(75)
t.backward(35)
t.right(100)
t.forward(15)
t.penup()
t.backward(35)
t.left(90)
t.forward(35)
t.left(90)
t.pendown()
n() #N
t.right(90)
t.penup()
t.forward(30)
t.right(90)
t.pendown()

 #K
t.forward(75)
t.backward(75/2)
t.left(30)
t.forward(45)
t.backward(45)
t.left(120)
t.forward(45)

t.penup()
t.right(45)
t.forward(10)
t.right(105)
t.forward(5)
t.pendown()
def h():
        t.forward(75) #H
        t.backward(75/2)
        t.left(90)
        t.forward(25)
        t.left(90)
        t.forward(75/2)
        t.backward(75)
h()
t.penup()
t.right(90)
t.forward(10)
t.pendown()

t.left(75)#A
t.forward(75)
t.right(155)
t.forward(75)
t.backward(35)
t.right(100)
t.forward(15)

t.penup()
t.backward(35)
t.left(90)
t.forward(35)
t.left(90)
t.pendown()
n() #N
t.pencolor('magenta')
t.penup()
t.backward(80)
t.left(90)
t.forward(450)
t.right(120)
t.forward(10)
t.pendown()
t.forward(20)


