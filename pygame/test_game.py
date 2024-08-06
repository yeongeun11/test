import pygame

## <<--- 초기화
pygame.init()
screen = pygame.display.set_mode((800, 600))

## <<-- fps 적용을 위한 시간 객체 생성
clock = pygame.time.Clock()
fps = 30
## -->>

x = screen.get_width()/2
y = screen.get_height()/2
redius = 40
speed = 10 

## <<---- 메인 루프
running = True
while running:
    for event in pygame.QUIT:
        running = False

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (255, 0, 0), (x, y), redius)

