import pygame

class Bullets(pygame.sprite.Sprite):
	"""Создание пуль персонажа"""

	def __init__(self, screen, player, stats):
		"""Инициализация данных"""
		super(Bullets, self).__init__()
		self.screen = screen
		self.player = player
		self.screen_rect = screen.get_rect()

		with open("files/num_bl.txt") as file:
			self.bullets_number = int(file.read())

		self.img = pygame.image.load(f"images/bullets/bullets{self.bullets_number}.png").convert_alpha()
		self.image = pygame.transform.scale(self.img, (10, 55))
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect()

		with open("files/bl_spd.txt", "r") as file:
			self.speed = float(file.read())
	
		self.rect.centerx = player.rect.centerx
		self.rect.centery = player.rect.centery
		self.y = float(self.rect.y)
		self.i = 0


	def update(self):
		"""Обновление движения пуль"""
		self.y -= self.speed
		self.rect.y = self.y

	def draw(self):
		"""Отображение пуль на экране"""
		self.screen.blit(self.image, self.rect)
			

	
