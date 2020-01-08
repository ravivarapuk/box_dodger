import random
import pygame
import math


def lvl(score, bomb_speed):
    """
    Defines the level(bomb_speed) corresponding to the score
    """
    if score < 300:
        bomb_speed = 2 + int(math.floor(score/20))
    else:
        bomb_speed = 2 + int(math.floor(score/10))
    return bomb_speed


def set_number_of_bombs(score):
    """
    Sets the number of bombs being gnerated as per the score of the player
    """
    if score < 101:
        return 3 + int(math.floor(score/10))
    else:
        return 14


def drop_bombs(score, bomb_list, width):
    """
    Generates a bomb list w.r.t the score of the player
    """
    randomize_fall = random.random()
    N = int(set_number_of_bombs(score))
    if len(bomb_list) < N and randomize_fall < 0.3:
        x_pos = random.randint(0, width-50)
        y_pos = 0
        bomb_list.append([x_pos, y_pos])


def draw_bombs(bomb_list, screen, bomb_size):
    """
    Draws/generates bombs on the canvas from top
    """
    for bomb_pos in bomb_list:
        pygame.draw.rect(screen, (204, 68, 0), (bomb_pos[0], bomb_pos[1], bomb_size, bomb_size))


def bomb_pos_increment(bomb_list, scr, height, bomb_speed):
    """
    Increments the position of the bomb (draws the bomb at new incremented co-ordinates
    """
    for index, bomb_pos in enumerate(bomb_list):
        if 0 <= bomb_pos[1] < height:
            bomb_pos[1] += bomb_speed
        else:
            bomb_list.pop(index)
            scr += 1
    return scr


def hit_check(player_pos, bomb_list, player_size):
    """
    To check if the bomb and the ship position overlaps
    """
    for bomb_pos in bomb_list:
        if hit_by_bomb_fr_sqr(player_pos, bomb_pos, player_size):
            return True
    return False


def hit_by_bomb_fr_sqr(p_pos, b_pos, player_size):
    """
    To check if the bomb was hit by square
    """
    p_x, p_y = p_pos[0], p_pos[1]
    b_x, b_y = b_pos[0], b_pos[1]

    if (p_x <= b_x < (p_x + player_size)) or (b_x <= p_x < (b_x + player_size)):
        if (p_y <= b_y < (p_y + player_size)) or (b_y <= p_y < (b_y + player_size)):
            return True

    return False
