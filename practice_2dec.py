#gracie oxnam
#functional structures


def x2_minus3x_plus4(x):
    y = x**2 - 3*x + 4
    return y

def quadratic(a,b,c,x):
    return (a*(x**2)) + b*x + c


print (x2_minus3x_plus4(15))
print (quadratic(a = 1,b = -3,c = 4,x = 0))


import turtle as t

world = t.Screen()
world.setup(400,400)

t.teleport(0,100)
t.goto(0,-100)
t.teleport(-100,0)
t.goto(100,0)

t.teleport(-30,x2_minus3x_plus4(-30))

for i in range (-30,30):
    t.goto(i,x2_minus3x_plus4(i))
