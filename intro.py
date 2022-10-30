import pygame, sys
import time
from pygame.locals import *
from pygame import freetype
import Summary
from GameLogic import GameLogic
import FirstStage
import GlobalVars

pygame.init()
screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)

font = 'helvetica'
ftypeinit = freetype.SysFont('Helvetica', 24)
fsize = 30

text = pygame.font.SysFont(font, 18).render("Press ESC to exit", True, (0, 0, 0))




while True:

    # Start Page
    screen.fill((255, 255, 255))
    x, y = screen.get_size()
    FirstStage.renderTextCenteredAt("Str00p Test\nby RYYYba", pygame.font.SysFont(font, fsize*4), (0, 0, 0), x / 2, y / 4, screen,
                         x / 1.5)
    FirstStage.renderTextCenteredAt("naciśnij start aby rozpocząć", pygame.font.SysFont(font, fsize), (0, 0, 0), x / 2,
                                    y / 1.5, screen,
                                    x / 1.5)
    # txt = pygame.font.SysFont(font, fsize*2).render("Str00p Test", True, (0, 0, 0))
    # text_rect = txt.get_rect(center=(x / 2, y / 2))
    # screen.blit(txt, text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                GlobalVars.score = 0
                Summary.run(screen, font, fsize, FirstStage.run(screen, font, fsize))
            elif event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.blit(text, (20, 20))

    pygame.display.flip()
