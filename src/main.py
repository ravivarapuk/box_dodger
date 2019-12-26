import random
import pygame
import sys
import game_dependencies as gm_deps

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

score, bomb_speed = 0, 1

screen = pygame.display.set_mode((width, height))

gm_over = False

clock = pygame.time.Clock()

endDispFont = pygame.font.SysFont("comicsansms", 21)


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

    if gm_deps.hit_by_bomb_fr_sqr(player_pos, bomb_pos):
        gm_over = True
        break

    gm_deps.drop_bombs(bomb_list, width)
    score = gm_deps.bomb_pos_increment(bomb_list, score, height, bomb_speed)

    bomb_speed = gm_deps.lvl(score, bomb_speed)

    text = "Score: " + str(score)
    lbl = endDispFont.render(text, 1, (255, 134, 0))
    screen.blit(lbl, (width-100, height-20))

    if gm_deps.hit_check(player_pos, bomb_list):
        gm_over = True
        break

    gm_deps.draw_bombs(bomb_list, screen)

    pygame.draw.rect(screen, (255, 0, 0), (player_pos[0], player_pos[1], 50, 50))

    clock.tick(30)

    pygame.display.update()
