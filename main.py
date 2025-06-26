from pygame import *
from spriteClass import Player
import time

# Colors
background = (200, 255, 255)
text_color = (255, 0, 0)

# Dimensions
width = 600
height = 500

# Window setup
window = display.set_mode((width, height))
clock = time.Clock()
font.init()
font1 = font.SysFont('Arial', 50)

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

# Ball speed
ball_speed_x = 3
ball_speed_y = 3

def reset_positions():
    ball.rect.x = 200
    ball.rect.y = 200
    pad1.rect.y = 220
    pad2.rect.y = 200

# Game state
run = True

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

    # Losing condition for Player 1
    if ball.rect.left <= 0:
        lose_text = font1.render("Player 1 Lost!", True, text_color)
        window.blit(lose_text, (width // 2 - lose_text.get_width() // 2, height // 2 - lose_text.get_height() // 2))
        display.update()
        time.sleep(2)
        reset_positions()

    # Losing condition for Player 2
    elif ball.rect.right >= width:
        lose_text = font1.render("Player 2 Lost!", True, text_color)
        window.blit(lose_text, (width // 2 - lose_text.get_width() // 2, height // 2 - lose_text.get_height() // 2))
        display.update()
        time.sleep(2)
        reset_positions()

    # Draw ball
    ball.reset(window)

    display.update()
    clock.tick(60)
