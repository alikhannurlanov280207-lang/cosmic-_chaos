import pygame.font
from pygame.sprite import Group

class Score:
	"""Вывод статистики"""

	def __init__(self, screen, stats):
		"""Инициализация данных"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.stats = stats
		self.text_color = (0, 255, 0)
		self.font = pygame.font.SysFont(None, 35)
		self.white = (255, 255, 255)
		self.serye = (165, 165, 165)

		with open("files/pl_hd.txt", "r") as file:
			self.hard = int(file.read())
		with open("files/pl_hd.txt", "r") as file:
			self.size_hard = int(file.read())

		self.color = (0, 255, 0)
		self.height = 150
		self.image_score()
		self.bullets_score()
		self.coins_score()

	def image_score(self):
		"""Вывод статистики 'Счет' """

		self.score_img = self.font.render(str(self.stats.score), True, self.white, (0, 0, 0))
		self.score_rect = self.score_img.get_rect()
		self.score_rect.right = self.screen_rect.right - 5
		self.score_rect.top = 20

	def show_score(self):
		"""Вывод очков на экран"""
		self.screen.blit(self.score_img, self.score_rect)
		self.screen.blit(self.bullets_img, self.bullets_rect)
		self.screen.blit(self.coins_img, self.coins_rect)
		pygame.draw.rect(self.screen, self.color, (10, 10, self.hard, 20))
		pygame.draw.rect(self.screen, self.white, (10, 10, self.size_hard, 20), 2)

	def bullets_score(self):
		"""Создание значения пуль в игре"""
		self.bullets_img = self.font.render(str(self.stats.bullets_volume), True, self.text_color, (0, 0, 0))
		self.bullets_rect = self.bullets_img.get_rect()
		self.bullets_rect.right = self.screen_rect.right - 50
		self.bullets_rect.top = self.screen_rect.bottom - 35

	def coins_score(self):
		# Создание значения бутка в игре
		self.coins_img = self.font.render(str(self.stats.coin), True, self.serye, (0, 0, 0))
		self.coins_rect = self.coins_img.get_rect()
		self.coins_rect.right = self.screen_rect.right - 5
		self.coins_rect.top = 100