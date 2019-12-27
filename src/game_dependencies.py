import random
import pygame
import math


def lvl(score, bomb_speed):
    if score < 300:
        bomb_speed = 2 + int(math.floor(score/20))
    else:
        bomb_speed = 2 + int(math.floor(score/10))
    return bomb_speed


def set_number_of_bombs(score):
    return 3 + int(math.floor(score/50))


def drop_bombs(score, bomb_list, width):
    randomize_fall = random.random()
    N = int(set_number_of_bombs(score))
    if len(bomb_list) < N and randomize_fall < 0.3:
        x_pos = random.randint(0, width-50)
        y_pos = 0
        bomb_list.append([x_pos, y_pos])


def draw_bombs(bomb_list, screen, bomb_size):
    for bomb_pos in bomb_list:
        pygame.draw.rect(screen, (204, 68, 0), (bomb_pos[0], bomb_pos[1], bomb_size, bomb_size))


def bomb_pos_increment(bomb_list, scr, height, bomb_speed):
    for index, bomb_pos in enumerate(bomb_list):
        if 0 <= bomb_pos[1] < height:
            bomb_pos[1] += bomb_speed
        else:
            bomb_list.pop(index)
            scr += 1
    return scr


def hit_check(player_pos, bomb_list):
    for bomb_pos in bomb_list:
        if hit_by_bomb_fr_sqr(player_pos, bomb_pos):
            return True
    return False


def hit_by_bomb_fr_sqr(p_pos, b_pos):
    p_x, p_y = p_pos[0], p_pos[1]
    b_x, b_y = b_pos[0], b_pos[1]

    if (b_x >= p_x and b_x < (p_x + 50)) or (p_x >= b_x and p_x < (b_x + 50)):
        if (b_y >= p_y and b_y < (p_y + 50)) or (p_y >= b_y and p_y < (b_y + 50)):
            return True

    return False
