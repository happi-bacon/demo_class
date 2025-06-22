from pygame import *
from spriteClass import Player

''' colors '''
background = (200, 255, 255)

'''var'''
width = 600
height = 500


window = display.set_mode(width, height)
window.fill(background)

clock = time.Clock()

pad1 = Player(player_image='images/pad.jpg',
              player_x=20, player_y=220, 
              player_speed=4, width=50, height=150)

pad2 = Player(player_image='images/pad.jpg',
              player_x=500, player_y=200, 
              player_speed=4, width=50, height=150)

ball = Player(player_image='images/ball.jpg',
              player_x=200, player_y=200, 
              player_speed=4, width=65, height=65)



run = True
finish = True
ball_speed_x = 1
ball_speed_y = 1

while run:

    if finish == True:
        window.fill(background)

        pad1.reset(window=window)
        pad1.update_left()

        pad2.reset(window=window)
        pad2.update_right()

        ball.reset(window=window)

        ball.rect.x += ball_speed_x
        ball.rect.y += ball_speed_y

        if ball.rect.y > 500-65 or ball.rect.y < 0:
            ball_speed_y *= 1

        if sprite.collide.rect(pad1, ball) or sprite.collide.rect.(pad2, ball):
            ball_speed_x *= -1


    if ball.rect.y > 65

    for e in event.get():
        if e.type == QUIT():
            run = False

            
    display.update()
    clock.tick(60)