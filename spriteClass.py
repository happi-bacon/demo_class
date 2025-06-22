from pygame import *


class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,player_speed, 
                 width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width,height))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

        self.missed_score = 0

        self.bullet_group = sprite.Group()

    def reset(self, window):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(Gamesprite):
    pass