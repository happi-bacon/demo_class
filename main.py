from pygame import *

''' colors '''
background = (200, 255, 255)

'''var'''
width = 600
height = 500


window = display.set_mode(width, height)
window.fill(background)

clock = time.Clock()



run = True

while run:

    for e in event.get():
        if e.type == QUIT():
            run = False

            
    display.update()
    clock.tick(60)