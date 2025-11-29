import pygame

class Statistics:
	"""Создание всей статистики игры"""

	def __init__(self):
		"""Инициализация данных"""

		with open("files/hts.txt", "r") as file:
			hearts = int(file.read())

		with open("files/btc.txt", "r") as file:
			coin = int(file.read())

		with open("files/bl_add.txt", "r") as file:
			bl_add = int(file.read())

	
		self.run_game = "start"
		self.pause = False
		
		self.fonvolume = 0.2
		self.objectsvolume = 0.1

		self.reset_stats(hearts, coin, bl_add)


	def reset_stats(self, hearts, coin, bl_add):
		"""Статистика"""

		self.score = 0
		self.bullets_volume = bl_add
		self.player_left = hearts
		self.comets_left = 50
		self.coin = coin
		self.coin_check = 0
		self.number_bullets = 1
		self.i = 0
		self.check_start = True



	

	