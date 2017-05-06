import pygame
import random

class Win(pygame.sprite.Sprite):
	
	def __init__(self, gs, player):
		self.gs = gs
		self.img = pygame.image.load("sprites/ball.png")
		self.rect = self.img.get_rect()
		self.rect.center = self.gs.width/2, self.gs.height/2
		self.speed = 3

	def tick(self):
		directions = [1,-1]
		self.rect.centerx += random.choice(directions)*self.speed
		self.rect.centery += random.choice(directions)*self.speed
