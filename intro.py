import pygame, sys
from pygame.locals import *
from GameLogic import GameLogic
import FirstStage

pygame.init()
screen = pygame.display.set_mode((1000, 500), pygame.RESIZABLE)

font = 'arial'
fsize = 30

text = pygame.font.SysFont(font, 18).render("Press ESC to exit", True, (0, 0, 0))




while True:

    # Start Page
    screen.fill((255, 255, 255))
    x, y = screen.get_size()
    screen.blit(pygame.font.SysFont(font, 30).render("Aby rozpocząć wciśnij spację", True, (0, 0, 0)),
                (round(x / 2) - 150, round(y / 2)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                FirstStage.run(screen, font, fsize)
            elif event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.blit(text, (20, 20))

    pygame.display.flip()
