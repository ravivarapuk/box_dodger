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
bomb_list = [bomb_pos]
bomb_speed = 9

screen = pygame.display.set_mode((width, height))

gm_over = False

clock = pygame.time.Clock()


def drop_bombs(bomb_list):
    if len(bomb_list) < 10:
        x_pos = random.randint(0, width-50)
        y_pos = 0
        bomb_list.append([x_pos, y_pos])


def draw_bombs(bomb_list):
    for bomb_pos in bomb_list:
        pygame.draw.rect(screen, (0, 0, 255), (bomb_pos[0], bomb_pos[1], 50, 50))


def bomb_pos_inc(bomb_list):
    for index, bomb_pos in enumerate(bomb_list):
        if 0 <= bomb_pos[1] < height:
            bomb_pos[1] += bomb_speed
        else:
            bomb_list.pop(index)


def hit_check(player_pos, bomb_list):
    for bomb_pos in bomb_list:
        if hit_by_bomb(player_pos, bomb_list):
            return True
    return False


def hit_by_bomb(p_pos, b_pos):
    p_x, p_y = p_pos[0], p_pos[1]
    b_x, b_y = b_pos[0], b_pos[1]

    if (b_x >= p_x and b_x < (p_x + 50)) or (p_x >= b_x and p_x < (b_x + 50)):
        if (b_y >= p_y and b_y < (p_y + 50)) or (p_y >= b_y and p_y < (b_y + 50)):
            return True
    return False


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

    if hit_by_bomb(player_pos, bomb_pos):
        gm_over = True
        break

    drop_bombs(bomb_list)
    bomb_pos_inc(bomb_list)

    if hit_check(player_pos, bomb_list):
        gm_over = True
        break

    draw_bombs(bomb_list)

    pygame.draw.rect(screen, (255, 0, 0), (player_pos[0], player_pos[1], 50, 50))

    clock.tick(30)

    pygame.display.update()
