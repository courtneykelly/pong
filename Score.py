import pygame
import math

class Score(pygame.sprite.Sprite):
	def __init__(self, gs):
		self.gs = gs
		self.img1 = pygame.image.load("sprites/10.png")
		self.img2 = pygame.image.load("sprites/10.png")
		self.rect1 = self.img1.get_rect()
		self.rect1.centerx = self.gs.width/2
		self.rect1.centery = self.gs.height/2

		self.speeds = [-3, 3]
		self.move_speed_x = random.choice(self.speeds)
		self.move_speed_y = random.choice(self.speeds)