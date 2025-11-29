import pygame
from pygame.locals import *

pygame.init()

# Расположение спрайтов
img_dir = 'images/Explosion/'

# Окно
flags = FULLSCREEN | DOUBLEBUF # Двойная буферизация
screen = pygame.display.set_mode((0, 0), flags, 16)


class Explosion(pygame.sprite.Sprite):
	"""Взрыв"""

	def __init__(self, screen, center, size):
		"""Инициализация данных"""
		super(Explosion, self).__init__()

		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.size = size
		self.image = explosion_anim[self.size][0]
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.frame = 0
		self.last_update = pygame.time.get_ticks()
		self.frame_rate = 50

	def update(self):
		"""Обновление спрайта взрыва"""
		now = pygame.time.get_ticks()

		if now - self.last_update > self.frame_rate:
			self.last_update = now
			self.frame += 1

			if self.frame == len(explosion_anim[self.size]):
				self.kill()
			else:
				center = self.rect.center
				self.image = explosion_anim[self.size][self.frame]
				self.rect = self.image.get_rect()
				self.rect.center = center

# Размеры взрыва
explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['md'] = []
explosion_anim['sm'] = []

# Перебор изображений
for i in range(1, 7):
	filename = 'Ex{}.png'.format(i)
	img = pygame.image.load(img_dir + filename).convert_alpha()
	img_lg = pygame.transform.scale(img, (230, 230))
	explosion_anim['lg'].append(img_lg)
	img_sm = pygame.transform.scale(img, (170, 170))
	explosion_anim['md'].append(img_sm)
	img_sm = pygame.transform.scale(img, (130, 130))
	explosion_anim['sm'].append(img_sm)