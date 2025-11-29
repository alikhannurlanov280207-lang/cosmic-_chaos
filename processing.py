import pygame
from stats import Statistics
import sys
import random
import shops
import time

stats = Statistics()
"""Обищие функции"""
def file_music():
	with open("files/sounds.txt", "w") as file:
		file.write("False")

def stars():
	# Звезды
	time_stars = pygame.USEREVENT + 1
	timer1 = pygame.time.set_timer(time_stars, 100)


""" Меню """
def music():
	# Музыка главного меню
	with open("files/sounds.txt", "r") as file:
		menus = file.read()

	if menus == "True":
		pygame.mixer.music.load("sounds/menu.mp3")
		pygame.mixer.music.set_volume(stats.fonvolume)
		pygame.mixer.music.play(-1)



def file_processing():
	# Обработка файлов (рекорд, пули)
	with open("files/rd.txt", "r") as file:
		record = file.read()

	with open("files/bl_ck.txt", "r") as file:
		bul_check = file.read()

	with open("files/gl.txt", "r") as files:
		purpose = int(files.read())


	return record, bul_check, purpose

def check():
	# Проверка пуль
	with open("files/bl_ck.txt", "r") as file:
		bulletscheks = int(file.read())
	
	for i in range(1, bulletscheks+1):
		if i != 1:
			with open(f"files/Bullets/bullets{i}.txt", "w") as bullets_file:
				bullets_file.write("True")

def exitis():
	# Выход из игры
	with open("files/sounds.txt", "w") as file:
		file.write("True")
	time.sleep(0.5)
	sys.exit()

"""Цикл главного меню"""

def highscore_file(record, purpose, bul_check):
	# Проверка цели и рекорда
	if int(record) >= purpose:
		with open("files/gl.txt", "w") as filess:
			filess.write(str(purpose+2000))
			with open("files/bl_ck.txt", "w") as bullets_file:
				if int(bul_check) < 6:
					bullets_file.write(str(int(bul_check)+1))
		check()


""" Игра """
def music_game():
	# Музка
	pygame.mixer.music.stop()
	pygame.mixer.music.load("sounds/run.mp3")
	pygame.mixer.music.set_volume(stats.fonvolume)
	pygame.mixer.music.play(-1)

def timer():
	# Таймера объектов
	time = random.randint(350, 800)# Comets
	time_comets = pygame.USEREVENT
	timer = pygame.time.set_timer(time_comets, time)

	time_stars = pygame.USEREVENT + 1 # Stars
	timer1 = pygame.time.set_timer(time_stars, 75)

	addbul = pygame.USEREVENT + 2 # AddBullets
	time_bul = random.randint(5000, 15000)
	timer_bul = pygame.time.set_timer(addbul, time_bul)






def cycle():
	# Файл
	with open("files/rd.txt", "r") as file:
		record = int(file.read())
		if stats.score > record:
			with open("files/rd.txt", "w") as file:
				file.write(str(stats.score))

def cycle_music():
	# Остановка музыки		
	with open("files/sounds.txt", "w") as file:
		file.write("True")
		pygame.mixer.music.stop()


""" Магазин скинов """

def files_skins():
	# Файлы выбора скина

	with open("files/Bullets/bullets2.txt", "r") as file2:
		fl_bl2 = file2.read()

	with open("files/Bullets/bullets3.txt", "r") as file3:
		fl_bl3 = file3.read()

	with open("files/Bullets/bullets4.txt", "r") as file4:
		fl_bl4 = file4.read()

	with open("files/Bullets/bullets5.txt", "r") as file5:
		fl_bl5 = file5.read()

	with open("files/Bullets/bullets6.txt", "r") as file6:
		fl_bl6 = file6.read()

	return fl_bl2, fl_bl3, fl_bl4, fl_bl5, fl_bl6

def shop_bullets(screen, W, H):
	# Изображения пуль
	bl1 = pygame.image.load(f"images/bullets/bullets1.png")
	bl2 = pygame.image.load(f"images/bullets/bullets2.png")
	bl3 = pygame.image.load(f"images/bullets/bullets3.png")
	bl4 = pygame.image.load(f"images/bullets/bullets4.png")
	bl5 = pygame.image.load(f"images/bullets/bullets5.png")
	bl6 = pygame.image.load(f"images/bullets/bullets6.png")

	screen.blit(bl1, (W//5,H//7))
	screen.blit(bl2, (W//3.4,H//7))
	screen.blit(bl3, (W//2.6,H//7))
	screen.blit(bl4, (W//1.6,H//7))
	screen.blit(bl5, (W//1.375,H//7))
	screen.blit(bl6, (W//1.2,H//7))

def check_bl(screen, W, H, bl_button, button, select, size):
	# Проверка на наличие пуль
	fl_bl2, fl_bl3, fl_bl4, fl_bl5, fl_bl6 = files_skins()

	if fl_bl2 == "True":
		bl_button.draw(W//3.5, H//3.5, select, size, shops.bullets2)
	else:
		button.print_text(screen, "Цель 1", W//3.5, H//3.5, 25)

	if fl_bl3 == "True":
		bl_button.draw(W//2.65, H//3.5, select, size, shops.bullets3)
	else:
		button.print_text(screen, "Цель 2", W//2.65, H//3.5, 25)

	if fl_bl4 == "True":
		bl_button.draw(W//1.61, H//3.5, select, size, shops.bullets4)
	else:
		button.print_text(screen, "Цель 3", W//1.61, H//3.5, 25)

	if fl_bl5 == "True":
		bl_button.draw(W//1.39, H//3.5, select, size, shops.bullets5)
	else:
		button.print_text(screen, "Цель 4", W//1.39, H//3.5, 25)

	if fl_bl6 == "True":
		bl_button.draw(W//1.21, H//3.5, select, size, shops.bullets6)
	else:
		button.print_text(screen, "Цель 5", W//1.21, H//3.5, 25)


""" Магазин улучшений """

def values():
	# Значения улучшений
	with open("files/pl_spd_pc.txt", "r") as file:
		player_price = int(file.read())

	with open("files/pl_spd.txt", "r") as file:
		playerspeed = float(file.read())

	with open("files/bl_spd_pc.txt", "r") as file:
		bullets_price = int(file.read())

	with open("files/bl_spd.txt", "r") as file:
		bulletsspeed = float(file.read())

	with open("files/hts.txt", "r") as file:
		hearts = int(file.read())

	with open("files/pl_lt_pc.txt", "r") as file:
		pl_left_price = int(file.read())

	with open("files/bl_add.txt", "r") as file:
		bl_add = int(file.read())

	with open("files/bl_add_pc.txt", "r") as file:
		bl_price = int(file.read())

	return player_price, playerspeed, bullets_price, bulletsspeed, hearts, pl_left_price, bl_add, bl_price


