import pygame
import math

class Player(pygame.sprite.Sprite):
	def __init__(self, gs, player_num):
		self.gs = gs
		self.img = pygame.image.load("sprites/player.png")
		self.rect = self.img.get_rect()
		if player_num == 1:
			self.rect.centerx = 10
			self.rect.centery = 235
		elif player_num == 2:
			self.rect.centerx = 630
			self.rect.centery = 235

		self.move_speed = 0

	def move(self, coord):
		self.rect = self.rect.move(coord)

	def tick(self):
		if self.rect.centery+self.move_speed >= 0 and self.rect.centery+self.move_speed <= self.gs.height:
			self.rect.centery += self.move_speed
