import pgzrun

def draw():
    screen.fill('white')
    screen.draw.filled_circle((150, 300), 50, 'red')
    screen.draw.filled_circle((400, 300), 50, 'yellow')
    screen.draw.filled_circle((650, 300), 50, 'blue')

pgzrun.go()

import pgzrun

# draw a face
def draw():
    screen.fill('white')
    screen.draw.filled_circle((300, 300), 300, 'blue')
    screen.draw.filled_circle((180, 150), 100, 'white')
    screen.draw.filled_circle((420, 150), 100, 'white')
    screen.draw.filled_circle((200, 180), 50, 'black')
    screen.draw.filled_circle((440, 180), 50, 'black')
    screen.draw.filled_circle((300, 280), 20, 'white')
    screen.draw.filled_circle((300, 450), 100, 'white')

pgzrun.go()


import pgzrun

r = 100
def draw():
    screen.fill('white')
    screen.draw.filled_circle((150, 300), r, 'red')
    screen.draw.filled_circle((400, 300), r, 'yellow')
    screen.draw.filled_circle((650, 300), r, 'blue')

pgzrun.go()

# gradually bigger circle
import pgzrun

r = 1
def draw():
    screen.fill('white')
    screen.draw.filled_circle((400, 300), r, 'red')
    
def update():
    global r 
    r += 5

pgzrun.go()



# gradually go to floor
import pgzrun

y  = 100
def draw():
    screen.fill('white')
    screen.draw.filled_circle((400, y), 30, 'red')
    
def update():
    global y 
    y += 1

pgzrun.go()





# repeatedly go to floor
import pgzrun

y  = 100
def draw():
    screen.fill('white')
    screen.draw.filled_circle((400, y), 30, 'red')
    
def update():
    global y 
    y += 1
    if y >= 600:
        y = 30

pgzrun.go()