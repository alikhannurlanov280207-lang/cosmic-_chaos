# Кнопки для игры
import pygame
from stats import Statistics

stats = Statistics()

class Button():
	"""Создание класса кнопок"""

	def __init__(self, width, height, screen):
		"""Инициализация данных"""
		self.screen = screen
		self.width = width
		self.height = height
		self.inactive = (3, 3, 3)
		self.active = (15, 15, 15)
		self.clicked = False

	def draw(self, x, y, message, font_size, action=None):
		"""Обработка действия кнопки"""
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
			pygame.draw.rect(self.screen, self.active, (x, y, self.width, self.height))

			if click[0] == 1 and self.clicked == False:
				self.clicked = True
				if action is not None:
					clicks = pygame.mixer.Sound("sounds/button.mp3")
					clicks.set_volume(stats.objectsvolume)
					clicks.play()
					action()
				self.clicked = False
		else:
			pygame.draw.rect(self.screen, self.inactive, (x, y, self.width, self.height))

		print_text(self.screen, message, x, y, font_size)


def print_text(screen, message, x, y, font_size, font_color=(255, 255, 255), font_type = "None"):
	"""Печать текст на экран"""
	font_type = pygame.font.SysFont(font_type, font_size)
	text = font_type.render(message, True, font_color)
	screen.blit(text, (x, y))