import pygame
from pygame.locals import *
from pygame.sprite import Group
import sys
import time
import random

import controls
from player import Player
from stats import Statistics
from score import Score
import button
import shops
import processing

# Инициализация pygame и обработка звука
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()




# Создание главного окна
flags = FULLSCREEN | DOUBLEBUF # Двойная буферизация
screen = pygame.display.set_mode((0, 0), flags, 16)

pygame.display.set_caption("Космическая битва")
pygame.display.set_icon(pygame.image.load("images/MainMenu/game.ico"))



# Размеры экрана
W, H = screen.get_size()

# Главные функции игры
def initial_screen():
	""" Начальный загрузочный экран """
	x = 0

	while x <= 150:
		time.sleep(0.005)
		if x == 0:
			time.sleep(1.0)
			x += 1
		else:
			x += 1
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()



		screen.fill((0, 0, 0))
		# Полоса загрузки
		pygame.draw.rect(screen, (255, 255, 255), (W//2 - 100, H//2 + 50, x, 20))
		pygame.draw.rect(screen, (255, 255, 255), (W//2 - 100, H//2 + 50, 150, 20), 2)

		button.print_text(screen, "Загрузка...", W//2 - 75, H//2, 30)
		

		pygame.display.update()
		pygame.display.flip()



	menu()


def menu():
	# Задержка
	time.sleep(0.075)

	""" Главное меню """
	
	# Изображения
	player = pygame.image.load("images/player/player.png")
	plnet_1 = pygame.image.load("images/MainMenu/planet1.png")
	plnet_2 = pygame.image.load("images/MainMenu/planet2.png")
	plnet_3 = pygame.image.load("images/MainMenu/planet3.png")
	

	stats = Statistics()
	score = Score(screen, stats)
	stars = Group()

	# Функции processing
	processing.music()

	processing.stars()


	# Координаты
	x = 50
	y_start = 300
	y_shop = 400
	y_exit = 500
	y_author = H - 60
	x_author = 20

	# Кнопки
	start_button = button.Button(155, 45, screen)
	exit_button = button.Button(150, 45, screen)
	shop_button = button.Button(190, 45, screen)
	author_button = button.Button(75, 30, screen)
	
	

	# Вечный цикл главного меню
	while 1:
		screen.fill((0, 0, 0))

		record, bul_check, purpose = processing.file_processing()

		processing.highscore_file(record, purpose, bul_check)
		controls.update_menu(screen, stars)
		stars.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		
			if event.type == pygame.USEREVENT + 1:
				controls._stars(screen, stars, W)
		
		# Изображения
		screen.blit(player, (W//2, H//2))
		screen.blit(plnet_3, (W//4, H//2))
		screen.blit(plnet_2, (W//2, H-H/1.1))
		screen.blit(plnet_1, (W//1.15, H//1.2))

		# Кнопки
		start_button.draw(x, y_start, "Играть", 55, run)
		shop_button.draw(x, y_shop, "Магазин", 55, shop)
		exit_button.draw(x, y_exit, "Выйти", 55, processing.exitis)
		author_button.draw(x_author, y_author, "Автор", 35, authors)

		# Тексты
		button.print_text(screen, "Космический Хаос", 10, 50, 100)
		button.print_text(screen, f"Рекорд: {str(record)}", W//1.3, H//3, 50)
		button.print_text(screen, f"Цель: {str(purpose)}", W//1.3, H//3 + 100, 50)

		if purpose >= 3000:
			purp = "Максимальная цель достигнута"
		else:
			purp = str(purpose)

		pygame.display.update()
		pygame.display.flip()
		




def game_over():
	""" Проигрыш """
	time.sleep(0.075)\
     

	stats = Statistics()

	fon = pygame.image.load("images/MainMenu/fonmenu.png")
	fon = pygame.transform.scale(fon, (W,H))

	text1 = "Вы проиграли..."
	text2 = "Чтобы начать игру заново, нажмите Enter, Esc — для выхода в главное меню"

	while 1:
		for event in pygame.event.get():
			if event == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					run()
					break
				if event.key == pygame.K_ESCAPE:
					menu()
					break

		screen.blit(fon, (0, 0))

		button.print_text(screen, text1, 550, 350, 50)
		button.print_text(screen, text2, 340, 450, 30)

		pygame.display.update()


def run():
	""" Запуск игры """

	# Функции
	processing.music_game()
	processing.timer()
	
	# Объкты
	player = Player(screen)
	stats = Statistics()
	score = Score(screen, stats)

	# Группы объектов
	bullets = Group()
	comets = Group()
	stars = Group()
	coins = Group()
	addbullets = Group()
	explosions = Group()
	
	# Пауза и цикл
	stats.pause = False
	while 1:
		controls.events(screen, player, bullets, comets, stats, score, button, stars, addbullets)

		if stats.run_game == "start":
			controls.update(screen, player, bullets, comets, score, stats, stars, addbullets, coins, explosions)
			controls.update_bullets(screen, bullets, comets, stats, score, coins, explosions)
			controls.update_comets(screen, comets, player, bullets, stats, score, stars, addbullets, coins, explosions)
			controls.update_player(screen, player, addbullets, stats, coins, score)
			player.update_player()	
		elif stats.run_game == "end":
			processing.cycle()
			game_over()
		else:
			processing.cycle()
			processing.cycle_music()
			menu()
			
			


def authors():
	""" Авторское окно """
	time.sleep(0.075)

	processing.file_music()
	processing.stars()

	stats = Statistics()
	stars = Group()

	player = pygame.image.load("images/player/player.png")
	bullet = pygame.image.load("images/bullets/bullets1.png")
	comet = pygame.image.load("images/comets/comet1.png")


	# Текста
	text = "Автор: Ваше имя."
	text3 = "Геймплей игры состоит из набора очков, получаемых за уничтожение комет."
	text4 = "В вашем космолёте есть пули, используйте их для защиты."
	text5 = "Также из комет выпадает валюта 'Byt' или 'Koines', которую можно потратить в магазине."
	text6 = "В магазине есть два раздела: для выбора и улучшения скинов, а также для улучшения космолёта."
	text7 = "На главном экране отображаются рекорд и Цель. Ставьте новые цели и побеждайте!"
	text8 = "За рекорды и выполненные цели в магазине открываются новые предметы."
	text9 = "Удачной игры!!!"


	back_button = button.Button(35, 35, screen)

	

	while 1:
		screen.fill((0, 0, 0))

		for event in pygame.event.get():
			if event == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					menu()
					break
			if event.type == pygame.USEREVENT + 1:
				controls._stars(screen, stars, W)

		controls.update_menu(screen, stars)
		stars.update()	

		# Изображения
		screen.blit(player, (W//1.2, H//1.3))
		screen.blit(bullet, (W//1.165, H//1.45))
		screen.blit(comet, (W//1.2, H//1.65))

		button.print_text(screen, "Авторство", W // 2 - 60, 50, 60)
		back_button.draw(10, 20, " <", 45, menu)

		# Текста
		button.print_text(screen, text, W // 2 - 450, H // 2 - 110, 30)
		button.print_text(screen, text3, W // 2 - 450, H // 2 - 40, 30)
		button.print_text(screen, text4, W // 2 - 450, H // 2 - 20, 30)
		button.print_text(screen, text5, W // 2 - 450, H // 2, 30)
		button.print_text(screen, text6, W // 2 - 450, H // 2 + 20, 30)
		button.print_text(screen, text7, W // 2 - 450, H // 2 + 40, 30)
		button.print_text(screen, text8, W // 2 - 450, H // 2 + 60, 30)
		button.print_text(screen, text9, W // 2 - 450, H // 2 + 80, 30)

		
		

		pygame.display.flip()
		pygame.display.update()
			
def shop():
	"""Магазин"""
	time.sleep(0.075)

	# Buttons
	button_improvement = button.Button(255, 45, screen)
	button_skins = button.Button(155, 45, screen)
	back_button = button.Button(35, 35, screen)

	stats = Statistics()
	stars = Group()

	processing.file_music()
	processing.stars()

	# images
	improvement = pygame.image.load("images/MainMenu/fon_improvement.png")
	skins = pygame.image.load("images/MainMenu/fon_skins.png")

	# coordinates
	x = W//1.485
	y_start = H // 1.2

	# Цикл магазина
	while 1:
		screen.fill((0, 0, 0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					menu()		
			if event.type == pygame.USEREVENT + 1:
				controls._stars(screen, stars, W)

		controls.update_menu(screen, stars)
		stars.update()	

		# Изображения
		screen.blit(improvement, (W//1.5,H//7))
		screen.blit(skins, (W//7,H//7))

		# Текст
		button.print_text(screen, "Магазин", W//2.2, 50, 60)

		# Кнопки
		button_improvement.draw(x, y_start, "Улучшения", 60, shop_improvement)
		button_skins.draw(W//5.5, H//1.2, "Скины", 60, shop_skins)
		back_button.draw(10, 20, " <", 45, menu)

		pygame.display.flip()
		pygame.display.update()

def shop_skins():
	"""Магазин скинов"""
	time.sleep(0.075)

	stats = Statistics()
	stars = Group()

	processing.stars()

	player_skins = pygame.image.load("images/MainMenu/playerskins.png")
	bullets_skins = pygame.image.load("images/MainMenu/bulletsskins.png")

	pl_button = button.Button(175, 35, screen)
	bl_button = button.Button(75, 35, screen)
	back_button = button.Button(35, 35, screen)

	select, size = "Выбор", 25
	
	# Цикл
	while 1:

		screen.fill((0, 0, 0))
		processing.shop_bullets(screen, W, H)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					shop()
			if event.type == pygame.USEREVENT + 1:
				controls._stars(screen, stars, W)

		controls.update_menu(screen, stars)
		stars.update()

		# Изображения
		screen.blit(player_skins, (W//15, H//1.5))
		screen.blit(bullets_skins, (W//15, H//7))

		# Кнопки
		back_button.draw(10, 20, " <", 45, shop)
		bl_button.draw(W//5.5, H//3.5, select, size, shops.bullets1)
		processing.check_bl(screen, W, H, bl_button, button, select, size)
		

		pygame.display.flip()
		pygame.display.update()


def shop_improvement():
	""" Магазин улучшений """
	time.sleep(0.075)

	stats = Statistics()
	stars = Group()

	player_skins = pygame.image.load("images/MainMenu/playerskins.png")
	bullets_skins = pygame.image.load("images/MainMenu/bulletsskins.png")

	player_button = button.Button(55, 35, screen)
	pl_left_button = button.Button(55, 35, screen)
	bullets_button = button.Button(55, 35, screen)
	back_button = button.Button(35, 35, screen)

	processing.stars()

	with open("files/btc.txt", "r") as file:
		coin = int(file.read())


	def player():
		# Покупка скорости игрока
		time.sleep(0.075)

		with open("files/pl_spd.txt", "r") as file:
			speed = float(file.read())
			with open("files/pl_spd.txt", "w") as files:
				files.write(str(float(speed) + 0.5))

		with open("files/pl_spd_pc.txt", "r") as file:
			price = int(file.read())
			with open("files/pl_spd_pc.txt", "w") as files:
				files.write(str(price + 50))

		with open("files/btc.txt", "w") as files:
			files.write(str(coin - price))
			stats.coin -= price


	def pl_left():
		# Покупка доп.жизней игрока
		time.sleep(0.075)
		hard = open("files/pl_hd.txt", "r")
		read_hard = int(hard.read())
		hards = open("files/pl_hd.txt", "w")

		with open("files/hts.txt", "r") as file:
			hearts = int(file.read())
			with open("files/hts.txt", "w") as files:
				files.write(str(int(hearts) + 10))

		with open("files/pl_lt_pc.txt", "r") as file:
			price = int(file.read())
			with open("files/pl_lt_pc.txt", "w") as files:
				files.write(str(price + 150))

		with open("files/btc.txt", "w") as files:
			files.write(str(coin - price))
			stats.coin -= price

		hards.write(str(read_hard + 15))
		hard.close()
		hards.close()


	def bullets():
		# Покупка скорости пуль
		time.sleep(0.075)
		with open("files/bl_spd.txt", "r") as file:
			speed = float(file.read())
			with open("files/bl_spd.txt", "w") as files:
				files.write(str(speed + 0.5))

		with open("files/bl_spd_pc.txt", "r") as file:
			price = int(file.read())
			with open("files/bl_spd_pc.txt", "w") as files:
				files.write(str(price + 50))

		with open("files/btc.txt", "w") as files:
			files.write(str(coin - price))
			stats.coin -= price


	def bl_adds():
		# Покупка доп.пули
		time.sleep(0.075)
		with open("files/bl_add.txt", "r") as file:
			adds = int(file.read())
			with open("files/bl_add.txt", "w") as files:
				files.write(str(adds + 2))

		with open("files/bl_add_pc.txt", "r") as file:
			price = int(file.read())
			with open("files/bl_add_pc.txt", "w") as files:
				files.write(str(price + 100))

		with open("files/btc.txt", "w") as files:
			files.write(str(coin - price))
			stats.coin -= price


	# Цикл
	while 1:
		player_price, playerspeed, bullets_price, bulletsspeed, hearts, pl_left_price, bl_add, bl_price = processing.values()

		screen.fill((0, 0, 0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					shop()


		# Player
		screen.blit(player_skins, (W//12, H//6))
		button.print_text(screen, f"Скорость: {playerspeed}", W//20, H//3, 40)
		button.print_text(screen, "Цена:", W//20, H//2.5, 40)
		
		button.print_text(screen, f"Жизнь: {hearts}", W//20, H//2, 40)
		button.print_text(screen, "Цена:", W//20, H//1.8, 40)

		# Покупка связанные с игроком
		if stats.coin >= player_price and playerspeed < 7.0:
			player_button.draw(W//7, H//2.5, str(int(player_price)), 45, player)
		elif playerspeed >= 7.0:
			button.print_text(screen, "Maks.", W//7, H//2.5, 40)
		else:
			button.print_text(screen, str(int(player_price)), W//7, H//2.5, 40)

		if stats.coin >= pl_left_price and hearts < 200:
			pl_left_button.draw(W//7, H//1.8, str(int(pl_left_price)), 45, pl_left)
		elif hearts >= 200:
			button.print_text(screen, "Maks.", W//7, H//1.8, 40)
		else:
			button.print_text(screen, str(int(pl_left_price)), W//7, H//1.8, 40)



		# Пули:
		screen.blit(bullets_skins, (W//1.45, H//6))
		button.print_text(screen, f"Скорость: {bulletsspeed}", W//1.5, H//3, 40)
		button.print_text(screen, "Цена:", W//1.5, H//2.5, 40)

		button.print_text(screen, f"Доп. пули: {bl_add}", W//1.5, H//2, 40)
		button.print_text(screen, "Цена:", W//1.5, H//1.8, 40)


		# Покупка связанные с пулями
		if stats.coin >= bullets_price and bulletsspeed < 9.0:
			bullets_button.draw(W//1.28, H//2.5, str(int(bullets_price)), 45, bullets)
		elif bulletsspeed >= 9.0:
			button.print_text(screen, "Maks.", W//1.28, H//2.5, 40)
		else:
			button.print_text(screen, str(int(bullets_price)), W//1.28, H//2.5, 40)


		if stats.coin >= bl_price  and bl_add < 30:
			bullets_button.draw(W//1.28, H//1.8, str(int(bl_price)), 45, bl_adds)
		elif bl_add >= 30:
			button.print_text(screen, "Maks.", W//1.28, H//1.8, 40)
		else:
			button.print_text(screen, str(int(bl_price)), W//1.28, H//1.8, 40)

		# Отображение текстов
		button.print_text(screen, "Улучшения", W//2.2, 50, 60)
		button.print_text(screen, f"Butk:  {stats.coin}", W/1.135, 99, 38)
		back_button.draw(10, 20, " <", 45, shop)
		pygame.display.flip()
		pygame.display.update()


# Вызов загрузочного экрана
if __name__ == "__main__":
	initial_screen()
 

	






