import pygame, sys
import time
from pygame.locals import *
from GameLogic import GameLogic
import FirstStage
import GlobalVars

pygame.init()
screen = pygame.display.set_mode((1268, 500), pygame.RESIZABLE)

font = 'helvetica'
fsize = 30

text = pygame.font.SysFont(font, 18).render("Press ESC to exit", True, (0, 0, 0))




while True:

    # Start Page
    screen.fill((255, 255, 255))
    x, y = screen.get_size()
    txt = pygame.font.SysFont(font, fsize*2).render("Aby rozpocząć naciśnij spację", True, (0, 0, 0))
    text_rect = txt.get_rect(center=(x / 2, y / 2))
    screen.blit(txt, text_rect)

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
