import pygame
import math

class Score(pygame.sprite.Sprite):
	def __init__(self, gs, player):
		self.gs = gs
		self.img = pygame.image.load("sprites/0.png")
		self.player = player
		self.rect = self.img.get_rect()
		self.score = 0

		if player == 1:
			self.rect.centerx = self.gs.width/2/2
			self.rect.centery = self.gs.height/2
		elif player == 2:
			self.rect.centerx = self.gs.width/2 + self.gs.width/2/2
			self.rect.centery = self.gs.height/2



	def increment_score(self):
		self.score+=1
		img_link = "sprites/" + str(self.score) + ".png"
		self.img = pygame.image.load(img_link)
		if self.score == 10:
			self.gs.stop = 1

	def tick(self):
		pass
