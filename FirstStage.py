import pygame, sys
from pygame.locals import *
from GameLogic import GameLogic
import GlobalVars


def run(screen, font, fsize):
    stage_1 = GameLogic()
    to_enter = stage_1.game_rounds(color_range=3,rounds=5)


    def level(lst) -> int:
        searched = lst[0]
        answers = lst[1]
        x, y = screen.get_size()
        searched_txt = pygame.font.SysFont(font, fsize*2).render(searched[0][0], True, searched[1][1])
        text_rect = searched_txt.get_rect(center=(x / 2, y/ 2.5))
        screen.blit(searched_txt, text_rect)

        corr_answ = -1
        it = 0
        labels = [
            'Z',
            'X',
            'C',
            'V'
        ]
        for i in answers:
            opt = i
            opt_txt = pygame.font.SysFont(font, fsize*2).render(opt[0][0], True, (0,0,0))
            if opt[0][0] == searched[0][0]:
                corr_answ = i
            text_rect = opt_txt.get_rect(center=(x * (it+1) / 5, y / 1.5))
            screen.blit(opt_txt, text_rect)

            opt_txt = pygame.font.SysFont(font, fsize * 2).render(labels[it], True, (0, 0, 0))
            text_rect = opt_txt.get_rect(center=(x * (it + 1) / 5, y / 1.2))
            screen.blit(opt_txt, text_rect)
            it += 1

        if corr_answ == -1:
            raise ValueError('No correct answer found')
        return corr_answ

    frame = 0
    GlobalVars.startTime = pygame.time.get_ticks()
    curr_stage = 0
    while True:
        frame += 1
        screen.fill((255, 255, 255))
        x, y = screen.get_size()
        if curr_stage == len(to_enter):
            for i in GlobalVars.firstStage:
                print(i)
            break
        corr_val = level(to_enter[curr_stage])

        text = pygame.font.SysFont(font, 18).render("Press ESC to exit", True, (0, 0, 0))
        screen.blit(text, (20, 20))
        text = pygame.font.SysFont(font, 18).render(str(frame), True, (0, 0, 0))
        screen.blit(text, (x-100, 20))
        # Start Page
        x, y = screen.get_size()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_z:
                    if corr_val == 0:
                        GlobalVars.firstStage.append([1, pygame.time.get_ticks(), to_enter[curr_stage][0]])
                        curr_stage += 1
                    else:
                        GlobalVars.firstStage.append([0, pygame.time.get_ticks(), to_enter[curr_stage][0]])
                        curr_stage += 1
                elif event.key == K_x:
                    if corr_val == 1:
                        GlobalVars.firstStage.append([1, pygame.time.get_ticks(), to_enter[curr_stage][0]])
                        curr_stage += 1
                    else:
                        GlobalVars.firstStage.append([0, pygame.time.get_ticks(), to_enter[curr_stage][0]])
                        curr_stage += 1
                elif event.key == K_c:
                    if corr_val == 2:
                        GlobalVars.firstStage.append([1, pygame.time.get_ticks(), to_enter[curr_stage][0]])
                        curr_stage += 1
                    else:
                        GlobalVars.firstStage.append([0, pygame.time.get_ticks(), to_enter[curr_stage][0]])
                        curr_stage += 1
                elif event.key == K_v:
                    if corr_val == 3:
                        GlobalVars.firstStage.append([1, pygame.time.get_ticks(), to_enter[curr_stage][0]])
                        curr_stage += 1
                    else:
                        GlobalVars.firstStage.append([0, pygame.time.get_ticks(), to_enter[curr_stage][0]])
                        curr_stage += 1
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
