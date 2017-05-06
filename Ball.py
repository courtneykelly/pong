import pygame
import math
import random

class Ball(pygame.sprite.Sprite):
	def __init__(self, gs):
		self.gs = gs
		self.img = pygame.image.load("sprites/ball.png")
		self.rect = self.img.get_rect()
		self.rect.centerx = self.gs.width/2
		self.rect.centery = self.gs.height/2

		self.speeds = [-3, 3]
		self.move_speed_x = random.choice(self.speeds)
		self.move_speed_y = random.choice(self.speeds)


	def move(self):
		self.rect.centerx += self.move_speed_x
		self.rect.centery += self.move_speed_y

	def reset(self):
		self.rect.centerx = self.gs.width/2
		self.rect.centery = self.gs.height/2
		self.move_speed_x = random.choice(self.speeds)
		self.move_speed_y = random.choice(self.speeds)		

	def tick(self):

		if ( self.rect.centerx + 15 < 0 ):
			self.gs.score2.increment_score()
			self.reset()
		elif ( self.rect.centerx - 15 > self.gs.width ):
			self.gs.score1.increment_score()
			self.reset()

		# Collisions with bar
		if ( self.rect.colliderect(self.gs.player1.rect) == True):
			self.move_speed_x = -self.move_speed_x
			self.move()
		elif ( self.rect.colliderect(self.gs.player2.rect) == True):
			self.move_speed_x = -self.move_speed_x
			self.move()
		# Collisions with top or bottom
		elif ( self.rect.centery + 20 >= self.gs.height ):
			self.move_speed_y = -self.move_speed_y
			self.move()

		elif ( self.rect.centery - 20 <= 0 ):
			self.move_speed_y = -self.move_speed_y
			self.move()
		else:
			self.move()


