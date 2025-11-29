import pygame


class Comets(pygame.sprite.Sprite):
	"""Создание препятствиям игроку 'Кометы' """

	def __init__(self, x, screen, group, rand, speedy, speedx, deg, size, images):
		"""Инциализация данных"""

		super(Comets, self).__init__()

		self.screen = screen
		self.screen_rect = screen.get_rect()

		self.image = images.convert_alpha()
		self.size = size
		self.img = pygame.transform.rotozoom(self.image, deg, self.size)
		self.mask = pygame.mask.from_surface(self.img)
		self.rect = self.img.get_rect(center=(x, -100))

		self.speedy = speedy
		self.speedx = speedx
		self.rect_y = 0
		self.rand = rand

		self.y = float(self.rect.y)
		self.x = float(self.rect.x)
		self.add(group)

	def update(self):
		"""Движение комет"""
		self.y += self.speedy
		self.rect.y = self.y

		if self.rand == 1:
			self.x += self.speedx
			self.rect.x = self.x
			
		if self.rand == 2:
			self.x -= self.speedx
			self.rect.x = self.x

	def draw(self):
		"""Отображение комет на экране"""
		self.screen.blit(self.img, self.rect)
  


class Comets(pygame.sprite.Sprite):
	"""Создание препятствиям игроку 'Кометы' """

	def __init__(self, x, screen, group, rand, speedy, speedx, deg, size, images):
		"""Инциализация данных"""

		super(Comets, self).__init__()

		self.screen = screen
		self.screen_rect = screen.get_rect()

		self.image = images.convert_alpha()
		self.size = size
		self.img = pygame.transform.rotozoom(self.image, deg, self.size)
		self.mask = pygame.mask.from_surface(self.img)
		self.rect = self.img.get_rect(center=(x, -100))

		self.speedy = speedy
		self.speedx = speedx
		self.rect_y = 0
		self.rand = rand

		self.y = float(self.rect.y)
		self.x = float(self.rect.x)
		self.add(group)

	def update(self):
		"""Движение комет"""
		self.y += self.speedy
		self.rect.y = self.y

		if self.rand == 1:
			self.x += self.speedx
			self.rect.x = self.x
			
		if self.rand == 2:
			self.x -= self.speedx
			self.rect.x = self.x

	def draw(self):
		"""Отображение комет на экране"""
		self.screen.blit(self.img, self.rect)
    
class Comet(pygame.sprite.Sprite):
    """Класс для комет"""

    def __init__(self, x, y, speedx, speedy, rand):
        super().__init__()
        self.image = pygame.image.load("assets/comet.png")
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speedx = speedx
        self.speedy = speedy
        self.rand = rand

    def update(self):
        """Движение комет"""
        self.y += self.speedy
        self.rect.y = self.y

        if self.rand == 1:
            self.x += self.speedx
            self.rect.x = self.x

        if self.rand == 2:
            self.x -= self.speedx
            self.rect.x = self.x

        # Увеличиваем скорость объектов, когда игрок набирает 500 очков
        if Comets.score >= 200:
            self.speedx *= 20.0
            self.speedy *= 25.5
            
        if Comets.score >= 400:
            self.speedx *= 90.0
            self.speedy *= 90.5
        
        if Comets.score >= 600:
            self.speedx *= 150.0
            self.speedy *= 150.5
            
        if Comets.score >= 800:
            self.speedx *= 250.0
            self.speedy *= 255.5
            
        if Comets.score >= 900:
            self.speedx *= 360.0
            self.speedy *= 365.5
            
        if Comets.score >= 1000:
            self.speedx *= 470.0
            self.speedy *= 475.5
        
