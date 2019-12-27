import random
import pygame
import sys
import game_dependencies as gm_deps

pygame.init()


if len(sys.argv) > 1:
    width, height = int(sys.argv[1]), int(sys.argv[2])
else:
    width, height = 650, 650


player_pos = [width/2, height-60]
player_size, bomb_size = 40, 20
bomb_pos = [random.randint(0, width-50), 0]
bomb_list = [bomb_pos]

score, bomb_speed = 0, 1

screen = pygame.display.set_mode((width, height))

gm_over = False

clock = pygame.time.Clock()

endDispFont = pygame.font.SysFont("comicsansms", 37)


while not gm_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x, y = player_pos[0], player_pos[1]

            if (event.key == pygame.K_LEFT) and x!= 0:
                x -= player_size
                print('Left Move', x)
            elif (event.key == pygame.K_RIGHT) and x!= (width-50):
                x += player_size
                print('Right Move', x)

            player_pos = [x, y]

    screen.fill((20, 154, 131))

    if gm_deps.hit_by_bomb_fr_sqr(player_pos, bomb_pos):
        gm_over = True
        break

    gm_deps.drop_bombs(score, bomb_list, width)
    score = gm_deps.bomb_pos_increment(bomb_list, score, height, bomb_speed)

    bomb_speed = gm_deps.lvl(score, bomb_speed)

    text = "Score: " + str(score)
    lbl = endDispFont.render(text, 1, (0, 0, 0))
    screen.blit(lbl, (width-130, height-25))

    if gm_deps.hit_check(player_pos, bomb_list):
        gm_over = True
        break

    gm_deps.draw_bombs(bomb_list, screen, bomb_size)

    pygame.draw.rect(screen, (255, 255, 255), (player_pos[0], player_pos[1], player_size, player_size))

    clock.tick(30)

    pygame.display.update()
