import pygame

pygame.init() #초기화 반드시 

# 화면 크기
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game") #게임이름

# 이벤트 루프
running = True # 게임이 진해주인가?
while running:
	for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
		if event.type == pygame.QUIT: # x버튼 눌러서 끄는경우, 창이 닫히는 이벤트가 발생하였는가?
 			running = False #게임이 진행중이 아님

# pygame 종료
pygame.quit()