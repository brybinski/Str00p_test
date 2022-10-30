import pygame, sys
from pygame.locals import *
from GameLogic import GameLogic
import GlobalVars


def run(screen, font, fsize):


    def level1(lst) -> int:
        searched = lst[0]
        answers = lst[1]
        x, y = screen.get_size()
        searched_txt = pygame.font.SysFont(font, fsize * 2).render(searched[0][0], True, searched[1][1])
        text_rect = searched_txt.get_rect(center=(x / 2, y / 2.5))
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
            opt_txt = pygame.font.SysFont(font, fsize * 2).render(opt[0][0], True, (0, 0, 0))
            if opt[0][0] == searched[0][0]:
                corr_answ = it
            text_rect = opt_txt.get_rect(center=(x * (it + 1) / 5, y / 1.5))
            screen.blit(opt_txt, text_rect)

            opt_txt = pygame.font.SysFont(font, fsize * 2).render(labels[it], True, (0, 0, 0))
            text_rect = opt_txt.get_rect(center=(x * (it + 1) / 5, y / 1.2))
            screen.blit(opt_txt, text_rect)
            it += 1

        if corr_answ == -1:
            raise ValueError('No correct answer found')
        return corr_answ

    GlobalVars.startTime = pygame.time.get_ticks()
    GlobalVars.firstStage.append(pygame.time.get_ticks())
    clock = pygame.time.Clock()
    time_now = 0

    # TODO: scoring system and timer
    def level2(lst):
        # color is important
        searched = lst[0]
        answers = lst[1]
        x, y = screen.get_size()
        searched_txt = pygame.font.SysFont(font, fsize * 2).render(searched[1][0], True, searched[0][1])
        text_rect = searched_txt.get_rect(center=(x / 2, y / 2.5))
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
            if opt[0][1] == searched[0][1]:
                corr_answ = it
            text_rect = pygame.Surface((100, 100)).get_rect(center=(x * (it + 1) / 5, y / 1.5))
            pygame.draw.rect(screen, opt[0][1], text_rect, width=0)

            opt_txt = pygame.font.SysFont(font, fsize * 2).render(labels[it], True, (0, 0, 0))
            text_rect = opt_txt.get_rect(center=(x * (it + 1) / 5, y / 1.2))
            screen.blit(opt_txt, text_rect)
            it += 1

        if corr_answ == -1:
            raise ValueError('No correct answer found')
        return corr_answ

    for level in level1, level2:
        curr_stage = 0
        stage_1 = GameLogic()
        to_enter = stage_1.game_rounds(color_range=4, rounds=5)
        end_stage = True
        corr_val = 0
        while end_stage:
            clock.tick()
            screen.fill((255, 255, 255))
            x, y = screen.get_size()
            if curr_stage == len(to_enter):
                print(GlobalVars.startTime)
                end_stage = False
                for i in GlobalVars.firstStage:
                    print(i)
            else:
                corr_val = level(to_enter[curr_stage])

            text = pygame.font.SysFont(font, 18).render("Press ESC to exit", True, (0, 0, 0))
            screen.blit(text, (20, 20))
            time_now += clock.get_rawtime()
            mins, txt_s, secs = GlobalVars.ms_to_mins(time_now)
            text = pygame.font.SysFont(font, 25).render(f'{mins}:{txt_s}:{secs}', True, (0, 0, 0))
            screen.blit(text, (x - 150, 20))

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
