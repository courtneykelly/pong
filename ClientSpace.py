import pygame
import math
from Player import Player
from Ball import Ball
from Score import Score

class ClientSpace:
	def __init__(self):
		# Initialize screen
		pygame.init()
		self.size = self.width, self.height = 640, 470
		self.black = 0, 0, 0
		self.screen = pygame.display.set_mode(self.size)
		background = pygame.image.load("sprites/background.png")

		# Initialize objects and clock
		self.spriteList = []
		self.player1 = Player(self, 1)
		self.player2 = Player(self, 2)
		self.ball = Ball(self)
		self.score1 = Score(self, 1)
		self.score2 = Score(self, 2)
		self.spriteList.append(self.player1)
		self.spriteList.append(self.player2)
		self.spriteList.append(self.ball)
		self.spriteList.append(self.score1)
		self.spriteList.append(self.score2)

		#self.clock = pygame.time.Clock()
		self.stop = 0

	def update_screen(self, objects):

		#self.clock.tick(60)
		for event in pygame.event.get():

			# If the user clicks out of the game
			if event.type == pygame.QUIT or self.stop == 1:
				exit(0)

			# If down or up arrow key is pressed
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					self.player2.move_speed = -5
					
				elif event.key == pygame.K_DOWN:
					self.player2.move_speed = 5
					
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					self.player2.move_speed = 0
					
				elif event.key == pygame.K_DOWN:
					self.player2.move_speed = 0

		# Update objects
		self.player1.center = objects['player1']
		self.player2.center = objects['player2']
		self.ball.center = objects['ball']
		self.score1.center = objects['score1']
		self.score2.center = objects['score2']
					


		# for sprite in self.spriteList:
		# 	sprite.tick()

		self.screen.fill(self.black)
		self.screen.blit(background,(0,0))

		for sprite in self.spriteList:
			self.screen.blit(sprite.img, sprite.rect)


		pygame.display.flip()

	# def main(self):

	# 	# Initialize screen
	# 	pygame.init()
	# 	self.size = self.width, self.height = 640, 470
	# 	self.black = 0, 0, 0
	# 	self.screen = pygame.display.set_mode(self.size)
	# 	background = pygame.image.load("sprites/background.png")

	# 	# Initialize objects and clock
	# 	self.spriteList = []
	# 	self.player1 = Player(self, 1)
	# 	self.player2 = Player(self, 2)
	# 	self.ball = Ball(self)
	# 	self.score1 = Score(self, 1)
	# 	self.score2 = Score(self, 2)
	# 	self.spriteList.append(self.player1)
	# 	self.spriteList.append(self.player2)
	# 	self.spriteList.append(self.ball)
	# 	self.spriteList.append(self.score1)
	# 	self.spriteList.append(self.score2)

	# 	self.clock = pygame.time.Clock()
	# 	self.stop = 0



	# 	while 1:
	# 		self.clock.tick(60)
	# 		for event in pygame.event.get():

	# 			# If the user clicks out of the game
	# 			if event.type == pygame.QUIT or self.stop == 1:
	# 				exit(0)

	# 			# If down or up arrow key is pressed
	# 			if event.type == pygame.KEYDOWN:
	# 				if event.key == pygame.K_UP:
	# 					self.player1.move_speed = -5
	# 					#self.player1.move([0,-5])
	# 				elif event.key == pygame.K_DOWN:
	# 					self.player1.move_speed = 5
	# 					#self.player1.move([0,5])
	# 			elif event.type == pygame.KEYUP:
	# 				if event.key == pygame.K_UP:
	# 					self.player1.move_speed = 0
	# 					#self.player1.move([0,0])
	# 				elif event.key == pygame.K_DOWN:
	# 					self.player1.move_speed = 0
	# 					#self.player1.move([0,0])


	# 		for sprite in self.spriteList:
	# 			sprite.tick()

	# 		self.screen.fill(self.black)
	# 		self.screen.blit(background,(0,0))

	# 		for sprite in self.spriteList:
	# 			self.screen.blit(sprite.img, sprite.rect)


	# 		pygame.display.flip()