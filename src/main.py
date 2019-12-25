import random
import pygame
import sys

pygame.init()

if len(sys.argv) > 1:
    width = sys.argv[1]
    height = sys.argv[1]
else:
    width = 600
    height = 500

player_pos = [width/2, height-2*50]

bomb_pos = [random.randint(0, width-50), 0]
bomb_speed = 9

screen = pygame.display.set_mode((width, height))

gm_over = False

clock = pygame.time.Clock()


def hit_bomb(p_pos, b_pos):
    p_x, p_y = p_pos[0], p_pos[1]
    b_x, b_y = b_pos[0], b_pos[1]


while not gm_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x, y = player_pos[0], player_pos[1]

            if event.key == pygame.K_LEFT:
                x -= 50
            elif event.key == pygame.K_RIGHT:
                x += 50

            player_pos = [x, y]

    screen.fill((0, 0, 0))

    if 0 <= bomb_pos[1] < height:
        bomb_pos[1] += bomb_speed
    else:
        bomb_pos[0] = random.randint(0, width-50)
        bomb_pos[1] = 0

    pygame.draw.rect(screen, (0, 0, 255), (bomb_pos[0], bomb_pos[1], 50, 50))
    pygame.draw.rect(screen, (255, 0, 0), (player_pos[0], player_pos[1], 50, 50))

    clock.tick(30)

    pygame.display.update()
