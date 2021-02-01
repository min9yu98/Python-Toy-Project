import pygame

pygame.init() #초기화 반드시 

# 화면 크기
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))


#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임이름

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\kmkkm\\Desktop\\python_dev\\pygame\\pygame_basic\\background.png")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load("C:\\Users\\kmkkm\\Desktop\\python_dev\\pygame\\pygame_basic\\character.png")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2)  - (character_width / 2) # 화면 '가로'의 절반 크기에 위치
character_y_pos = screen_height - character_height# 화면 '세로' 크기 가장 아래에 위치


# 이벤트 루프
running = True # 게임이 진해주인가?
while running:
	for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
		if event.type == pygame.QUIT: # x버튼 눌러서 끄는경우, 창이 닫히는 이벤트가 발생하였는가?
 			running = False #게임이 진행중이 아님

	screen.blit(background, (0, 0)) # 배경그리기
	screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기 
	pygame.display.update() # 게임화면 다시 그리기 (유지)

# pygame 종료
pygame.quit()