import pygame
import random
pygame.init()

score = 0

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("test")

clock = pygame.time.Clock()

background = pygame.image.load("C:\\Users\\kmkkm\\Desktop\\python_dev\\pygame_myself\\background.png")

character = pygame.image.load("C:\\Users\\kmkkm\\Desktop\\python_dev\\pygame_myself\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height
character_speed = 0.6
to_x = 0

randomNumber = 30
starSpeed = 10

star = pygame.image.load("C:\\Users\\kmkkm\\Desktop\\python_dev\\pygame_myself\\star.png")
star_size = star.get_rect().size
star_width = star_size[0]
star_height = star_size[1]
star_x_pos = 200
star_y_pos = 100

game_font = pygame.font.Font(None, 40)

totalTime = 10
startTicks = pygame.time.get_ticks()

running = True
while running:
	dt = clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				to_x -= character_speed
			elif event.key == pygame.K_RIGHT:
				to_x += character_speed

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				to_x = 0

	character_x_pos += to_x * dt

	if character_x_pos < 0:
		character_x_pos = 0
	elif character_x_pos > screen_width - character_width:
		character_x_pos = screen_width - character_width

	randomNumber = random.randrange(1, 200)
	randomNumber2 = random.randrange(1, 440)

	if star_y_pos > 640:
		star_y_pos = randomNumber
		star_x_pos = randomNumber2
		score += 1
		starSpeed += 2
	star_y_pos += starSpeed

	characterRect = character.get_rect()
	characterRect.left = character_x_pos
	characterRect.top = character_y_pos

	starRect = star.get_rect()
	starRect.left = star_x_pos
	starRect.top = star_y_pos

	if characterRect.colliderect(starRect):
		print("collision")
		running = False

	elapsedTime = (pygame.time.get_ticks()) / 1000
	timer = game_font.render(str(int(totalTime - elapsedTime)), True, (255, 255, 255))
	scores = game_font.render(str(score), True, (200, 200, 200))



	screen.blit(background, (0, 0))
	screen.blit(character, (character_x_pos, character_y_pos))
	screen.blit(star, (star_x_pos, star_y_pos))
	screen.blit(timer, (10, 10))
	screen.blit(scores, (10, 30))

	pygame.display.update()




pygame.quit()
