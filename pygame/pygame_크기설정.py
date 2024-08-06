import pygame

pygame.init()
 # 너비 800px, 높이 600px의 화면 생성
screen = pygame.display.set_mode((800, 600))

rurring = True
while rurring:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rurring = False

pygame.quit()