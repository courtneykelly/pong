import pygame
import math
from Player import Player
from Ball import Ball
from Score import Score
from Win import Win

class ClientSpace:
	def __init__(self):
		# Initialize screen
		pygame.init()
		self.size = self.width, self.height = 640, 470
		self.black = 0, 0, 0
		self.screen = pygame.display.set_mode(self.size)
		self.background = pygame.image.load("sprites/background.png")

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

		self.stop = 0
		self.win = 0

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
		self.player1.rect.center = objects['player1']
		self.ball.rect.center = objects['ball']

		self.score1.score = objects['score1']
		self.score2.score = objects['score2']
		self.win = objects['win']

		for sprite in self.spriteList:
			sprite.tick()

		self.screen.fill(self.black)
		self.screen.blit(self.background,(0,0))

		if self.win > 0:
			self.background = pygame.image.load("sprites/winner"+str(self.win)+".png")
			self.spriteList[:] = [] # empty sprite list
			for collin in range(100):
				win_screen = Win(self, self.win)
				self.spriteList.append(win_screen)

		for sprite in self.spriteList:
			self.screen.blit(sprite.img, sprite.rect)


		pygame.display.flip()
