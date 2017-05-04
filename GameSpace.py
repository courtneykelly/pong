import pygame
import math
from Player import Player

class GameSpace:
	def main(self):

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
		self.spriteList.append(self.player1)
		self.spriteList.append(self.player2)
		# self.lasers = []
		self.clock = pygame.time.Clock()
		# self.explosion = 0


		while 1:
			self.clock.tick(60)
			for event in pygame.event.get():

				# If the user clicks out of the game
				if event.type == pygame.QUIT:
					exit(0)

				# If down or up arrow key is pressed
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						self.player1.move([0,-5])
					elif event.key == pygame.K_DOWN:
						self.player1.move([0,5])
				elif event.type == pygame.KEYUP:
					if event.key == pygame.K_UP:
						self.player1.move([0,0])
					elif event.key == pygame.K_DOWN:
						self.player1.move([0,0])


			# 	# If the user shoots a laser
			# 	if event.type == pygame.MOUSEBUTTONDOWN:
			# 		if self.player.is_firing == False:
			# 			self.player.is_firing = True
			# 			self.player.mouse_x, self.player.mouse_y = pygame.mouse.get_pos()

			# for sprite in self.spriteList:
			# 	sprite.tick()

			self.screen.fill(self.black)
			self.screen.blit(background,(0,0))

			for sprite in reversed(self.spriteList):
				self.screen.blit(sprite.img, sprite.rect)


			pygame.display.flip()