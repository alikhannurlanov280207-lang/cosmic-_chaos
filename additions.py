import pygame


class AddBullets(pygame.sprite.Sprite):
	"""Добавления дополнительных пуль"""

	def __init__(self, screen, x, speedx, speedy, rand):
		"""Инициализирование данных"""
		super(AddBullets, self).__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.image = pygame.image.load("images/Improvements/addbullets.png").convert_alpha()
		self.mask = pygame.mask.from_surface(self.image)
		self.rect = self.image.get_rect(center=(x, -100))
		self.speedy = speedy
		self.speedx = speedx
		self.rand = rand
		self.y = float(self.rect.y)
		self.x = float(self.rect.x)


	def update(self):
		"""Обновление движение доп.пули"""
		self.y += self.speedy
		self.rect.y = self.y
		if self.rand == 1:
			self.x += self.speedx
			self.rect.x = self.x
			
		elif self.rand == 2:
			self.x -= self.speedx
			self.rect.x = self.x
		else:
			pass

	def draw_addbullet(self):
		"""Нарисовка пак доп. пуль"""
		self.screen.blit(self.image, self.rect)



class Healing(pygame.sprite.Sprite):
	"""Добавления дополнительных сердец"""

	def __init__(self, screen, x, speedx, speedy, rand):
		"""Инициализирование данных"""
		super(Healing, self).__init__()
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.image = pygame.image.load("images/healing.png")
		self.img = pygame.transform.rotozoom(self.image, 0, 2)
		self.mask = pygame.mask.from_surface(self.img)
		self.rect = self.img.get_rect(center=(x, 0))
		self.speedy = speedy
		self.speedx = speedx
		self.rand = rand
		self.y = float(self.rect.y)
		self.x = float(self.rect.x)


	def update(self):
		"""Обновление движение доп.сердец"""
		self.y += self.speedy
		self.rect.y = self.y
		if self.rand == 1:
			self.x += self.speedx
			self.rect.x = self.x
			
		elif self.rand == 2:
			self.x -= self.speedx
			self.rect.x = self.x
		else:
			pass

	def draw_healing(self):
		"""Нарисовка пак доп.сердец"""
		self.screen.blit(self.img, self.rect)