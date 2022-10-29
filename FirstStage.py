import pygame, sys
from pygame.locals import *
from GameLogic import GameLogic


def run(screen, font, fsize):
    stage_1 = GameLogic()
    to_enter = stage_1.game_rounds()

    def level(lst):
        searched = lst[0]
        answers = lst[1]
        x, y = screen.get_size()
        searched_txt = pygame.font.SysFont(font, fsize).render(searched[0][0], True, searched[1][1])
        screen.blit(searched_txt, (round(x / 2) - 150, round(y / 2)))

    while True:
        screen.fill((255, 255, 255))

        level(to_enter[0])
        text = pygame.font.SysFont(font, 18).render("Press ESC to exit", True, (0, 0, 0))
        screen.blit(text, (20, 20))
        # Start Page
        x, y = screen.get_size()


        pygame.draw.rect(screen, (0, 0, 255),
                         [100, 100, 400, 100], 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_x:
                    print('x was pressed')
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
