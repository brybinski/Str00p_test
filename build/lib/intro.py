import pygame, sys
import time
from pygame.locals import *
from pygame import freetype
import Summary
from GameLogic import GameLogic
import FirstStage
import GlobalVars
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox


def main():
    pygame.init()
    screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
    x, y = screen.get_size()
    slider = Slider(screen, int(x/6), int(y/4), int(25), int(y/2), vertical=True, handleRadius=int(x/40), min=4, max=10, step=1, initial=4)
    font = 'helvetica'
    ftypeinit = freetype.SysFont('Helvetica', 24)
    fsize = 30

    text = pygame.font.SysFont(font, 18).render("Press ESC to exit", True, (0, 0, 0))
    output = TextBox(screen, int(x/9), int(y/2), 50, 50, fontSize=30)

    output.disable()

    while True:
        # Start Page
        screen.fill((255, 255, 255))
        events = pygame.event.get()
        pygame_widgets.update(events)

        x, y = screen.get_size()
        FirstStage.renderTextCenteredAt("liczba kolorów", pygame.font.SysFont(font, fsize), (0, 0, 0),
                                        x / 10, y / 4, screen,
                                        x / 10)
        FirstStage.renderTextCenteredAt("Test Stroopa", pygame.font.SysFont(font, fsize * 4), (0, 0, 0),
                                        x / 2, y / 4, screen,
                                        x / 1.5)
        FirstStage.renderTextCenteredAt("naciśnij start aby rozpocząć", pygame.font.SysFont(font, fsize), (0, 0, 0),
                                        x / 2,
                                        y / 1.5, screen,
                                        x / 1.5)
        # txt = pygame.font.SysFont(font, fsize*2).render("Str00p Test", True, (0, 0, 0))
        # text_rect = txt.get_rect(center=(x / 2, y / 2))
        # screen.blit(txt, text_rect)
        output.setText(slider.getValue())
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    GlobalVars.score = 0
                    Summary.run(screen, font, fsize, FirstStage.run(screen, font, fsize, slider.getValue()),slider.getValue())
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.blit(text, (20, 20))
        pygame.display.flip()

main()