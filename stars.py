import pygame


class Stars(pygame.sprite.Sprite):
	"""Создание звезд"""

	def __init__(self, screen, x):
		"""Инциализация данных"""

		super(Stars, self).__init__()

		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.image = pygame.image.load(f"images/MainMenu/stars.png").convert_alpha()
		self.img = pygame.transform.rotozoom(self.image, 0, 0.5)
		self.rect = self.image.get_rect(center=(x, -50))
		self.speedy = 1.2
		
		self.y = float(self.rect.y)
		self.x = float(self.rect.x)
		

	def update(self):
		"""Движение звезд"""
		self.y += self.speedy
		self.rect.y = self.y


	def draw(self):
		"""Отображение звезды на экране"""
		self.screen.blit(self.img, self.rect)
		