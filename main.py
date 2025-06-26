from pygame import *
from spriteClass import Player

# Colors
background = (200, 255, 255)

# Dimensions
width = 600
height = 500

# Window setup
window = display.set_mode((width, height))
clock = time.Clock()

# Players and ball
pad1 = Player(player_image='images/pad.jpg',
              player_x=20, player_y=220, 
              player_speed=4, width=50, height=150)

pad2 = Player(player_image='images/pad.jpg',
              player_x=500, player_y=200, 
              player_speed=4, width=50, height=150)

ball = Player(player_image='images/ball.jpg',
              player_x=200, player_y=200, 
              player_speed=4, width=65, height=65)

# Game state
run = True
ball_speed_x = 3
ball_speed_y = 3

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.fill(background)

    # Move and draw paddles
    pad1.update_left()
    pad1.reset(window)

    pad2.update_right()
    pad2.reset(window)

    # Move ball
    ball.rect.x += ball_speed_x
    ball.rect.y += ball_speed_y

    # Bounce off top and bottom
    if ball.rect.top <= 0 or ball.rect.bottom >= height:
        ball_speed_y *= -1

    # Bounce off paddles
    if pad1.rect.colliderect(ball.rect) or pad2.rect.colliderect(ball.rect):
        ball_speed_x *= -1

    # Draw ball
    ball.reset(window)

    display.update()
    clock.tick(60)
