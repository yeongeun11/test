import pygame
import random

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("동그라미 이동 및 색상 변경 프로그램")

# 색상 정의
colors = [(255, 0, 0), (0, 0, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255)] # 빨간색, 검정색, 노란색, 녹색, 파란색
current_color = random.choice(colors)
circle_radius = 40

# 동그라미 초기 위치
circle_x = screen_width // 2
circle_y = screen_height // 2

# 프레임 레이트 설정
clock = pygame.time.Clock()
fps = 30

# 이동 속도 (픽셀 / 초)
speed = 300 # 10픽셀 * 30프레임 = 300픽셀/초

# 메인 루프
running = True
while running:
    # 델타 타임 계산
    delta_time = clock.tick(fps) / 1000.0

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # 왼쪽 버튼 클릭
                new_color = random.choice(colors)
                while new_color == current_color:
                    new_color = random.choice(colors)
                current_color = new_color

    # 키보드 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        circle_x -= speed * delta_time
    if keys[pygame.K_RIGHT]:
        circle_x += speed * delta_time
    if keys[pygame.K_UP]:
        circle_y -= speed * delta_time
    if keys[pygame.K_DOWN]:
        circle_y += speed * delta_time
