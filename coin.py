import pygame


class Coins(pygame.sprite.Sprite):
	"""Создание валюты 'Койны' """

	def __init__(self, screen, x, y):
		"""Инциализация данных"""

		super(Coins, self).__init__()

		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		self.image = pygame.image.load(f"images/coin.png").convert_alpha()
		self.img = pygame.transform.rotozoom(self.image, 0, 1)
		self.mask = pygame.mask.from_surface(self.img)
		self.rect = self.image.get_rect(center=(x, y))

		self.speedy = 0.8	
		self.y = float(self.rect.y)
		
	def update(self):
		"""Движение монет"""
		self.y += self.speedy
		self.rect.y = self.y

	def draw(self):
		"""Отображение монет на экране"""
		self.screen.blit(self.img, self.rect)