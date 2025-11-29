import pygame

class Player:
	"""Создание главного персонажа"""

	def __init__(self, screen):
		"""Инициализация данных"""
		self.screen = screen
		self.screen_rect = screen.get_rect()

		self.image = pygame.image.load("images/player/player.png").convert_alpha()
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect()

		self.rect.centerx = self.screen_rect.centerx 
		self.rect.centery = self.screen_rect.bottom - 40

		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)

		with open("files/pl_spd.txt", "r") as file:
			self.speed = float(file.read())

		self.mleft = False
		self.mright = False
		self.mtop = False
		self.mbottom = False
		self.mstop = False

	def update_player(self):
		"""Обновление движений игрока"""
		
		if self.mtop and self.rect.top > self.screen_rect.top:
			self.centery -= self.speed
			self.image = pygame.image.load("images/player/up.png")
		else:
			self.image = pygame.image.load("images/player/player.png")
		if self.mbottom  and self.rect.bottom < self.screen_rect.bottom:
			self.centery += self.speed
			self.image = pygame.image.load("images/player/down.png")
		if self.mleft and self.rect.left > self.screen_rect.left:
			self.centerx -= self.speed
			self.image = pygame.image.load("images/player/left.png")
		if self.mright and self.rect.right < self.screen_rect.right:
			self.centerx += self.speed
			self.image = pygame.image.load("images/player/right.png")
	
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery
		

	def draw(self):
		"""Отображение персонажа на экран"""
		self.screen.blit(self.image, self.rect)

	def create_player(self):
		"""Создание игрока после смерти"""
		self.centerx = self.screen_rect.centerx
		self.centery = self.screen_rect.bottom - 40
