import sys
from pygame.locals import *
import FirstStage
from datetime import datetime
import GlobalVars
import json
from operator import itemgetter
import pygame
from pygame import freetype

pygame.freetype.init()
BG_COLOR = pygame.Color((255, 255, 255))
BLUE = pygame.Color((0, 0, 0))
FONT = freetype.SysFont('Helvetica', 24)


def save(highscores):
    with open('highscores.json', 'w') as file:
        json.dump(highscores, file)  # Write the list to the json file.

def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file)  # Write the list to the json file.

def load():
    try:
        with open('highscores.json', 'r') as file:
            highscores = json.load(file)  # Read the json file.
    except FileNotFoundError:
        highscores = []  # Define an empty list if the file doesn't exist.
    # Sorted by the score.
    return sorted(highscores, key=itemgetter(1), reverse=True)


def run(screen, font, fsize, time_now):
    FONT = freetype.Font(None, 24)
    score = GlobalVars.score
    time = GlobalVars.ms_to_mins(time_now)
    name = ''
    highscores = load()  # Load the json file.

    entered = False
    finished = True
    while finished:
        screen.fill((255, 255, 255))
        sx, sy = screen.get_size()
        text = pygame.font.SysFont(font, 18).render("Press ESC to exit", True, (0, 0, 0))
        screen.blit(text, (20, 20))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and not entered:

                    highscores.append([name, score, time_now])
                    save(sorted(highscores, key=itemgetter(1), reverse=True))
                    name = ''
                    highscores = load()
                    entered = True
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]  # Remove the last character.
                elif event.key == K_ESCAPE:
                    save_data([GlobalVars.DataCollection, datetime.now()])
                    GlobalVars.DataCollection = []
                    GlobalVars.score = 0
                    finished = False
                else:
                    name += event.unicode  # Add a character to the name.

        for y, (hi_name, hi_score, atime) in enumerate(highscores):
            if y < 10:
                FONT.render_to(screen, (sx/4, sy * (y+1) / 11),
                               f'{y + 1}. {hi_name} {hi_score} {GlobalVars.ms_to_mins(atime)[0]}:{GlobalVars.ms_to_mins(atime)[1]}:{GlobalVars.ms_to_mins(atime)[2]}',
                               BLUE)

        FONT.render_to(screen, (sx / 1.5, sy * 11 / 14), f'Twój wynik to: {score}', BLUE)
        FONT.render_to(screen, (sx / 1.5, sy * 12 / 14), f'Twój czas to: {GlobalVars.ms_to_mins(time_now)[0]}:{GlobalVars.ms_to_mins(time_now)[1]}:{GlobalVars.ms_to_mins(time_now)[2]}', BLUE)
        if not entered:
            FONT.render_to(screen, (sx / 1.5, sy * 13 / 14), f'Wprowadź imię: {name}', BLUE)

        pygame.display.flip()
