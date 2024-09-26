import math

def move(x, y, step, angle=0):
    nx =x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

x = int(input('Please input x: '))
y = int(input('Please input y: '))

(nx,ny) = move(x, y, 60, math.pi/6)
print(nx,ny)
