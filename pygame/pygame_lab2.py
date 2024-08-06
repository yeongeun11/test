# 800x600 픽셀 크기의 파이게임 윈도우에서 다음기능을 구현하라 
# 프로그램이 실행될 때마다 화면에 무작위 위치에 무작위 크기와 색상의 원을 여러개 그린다 
# 각 원은 서로 다른 위치, 크기, 그리고 RGB 색상값을 가진다
# 원의 개수도 무작위로 결정된다(5~20)개

import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))

# 화면 초기화
screen.fill((255, 255, 255)) # 배경을 흰색으로 설정
pygame.display.flip()

# 원 그리기
num_circles = random.randint(5, 20) # 5에서 20 사이의 원 개수
for _ in range(num_circles):
    radius = random.randint(10, 100) # 반지름을 10에서 100 사이로 설정
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # 화면 내에서 무작위 위치
    position = (random.randint(0 + radius, 800 - radius), random.randint(0 + radius, 600 - radius))

    pygame.draw.circle(screen, color, position, radius)

pygame.display.flip() # 화면 업데이트

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()