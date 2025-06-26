from pygame import *
from spriteClass import Player

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
reset_timer = 0
loser = ""

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.fill(background)

    if reset_timer == 0:
        # Normal game logic
        pad1.update_left()
        pad1.reset(window)

        pad2.update_right()
        pad2.reset(window)

        ball.rect.x += ball_speed_x
        ball.rect.y += ball_speed_y

        if ball.rect.top <= 0 or ball.rect.bottom >= height:
            ball_speed_y *= -1

        if pad1.rect.colliderect(ball.rect) or pad2.rect.colliderect(ball.rect):
            ball_speed_x *= -1

        # Losing conditions
        if ball.rect.left <= 0:
            loser = "Player 1 Lost!"
            reset_timer = pygame.time.get_ticks() + 2000  # 2 seconds delay
        elif ball.rect.right >= width:
            loser = "Player 2 Lost!"
            reset_timer = pygame.time.get_ticks() + 2000

    else:
        # During delay, show losing message
        text = font1.render(loser, True, text_color)
        window.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
        if pygame.time.get_ticks() >= reset_timer:
            reset_positions()
            reset_timer = 0

    ball.reset(window)
    display.update()
    clock.tick(60)

