import pygame
import sys
from pygame.locals import *
from GameLogic import GameLogic
import GlobalVars


def renderTextCenteredAt(text, font, colour, x, y, screen, allowed_width):
    # first, split the text into words
    lst_of_br = []
    it = 0
    for i in range(0, len(text)):
        if text[i] == '\n':
            lst_of_br.append(text[it:i].split())
            it = i
    if it < len(text)-1:
        lst_of_br.append(text[it:].split())

    # now, construct lines out of these words
    lines = []
    for words in lst_of_br:
        while len(words) > 0:
            # get as many words as will fit within allowed_width
            line_words = []
            while len(words) > 0:
                line_words.append(words.pop(0))
                fw, fh = font.size(' '.join(line_words + words[:1]))
                if fw > allowed_width:
                    break

            # add a line consisting of those words
            line = ' '.join(line_words)
            lines.append(line)

    # now we've split our text into lines that fit into the width, actually
    # render them

    # we'll render each line below the last, so we need to keep track of
    # the culmative height of the lines we've rendered so far
    y_offset = 0
    for line in lines:
        fw, fh = font.size(line)

        # (tx, ty) is the top-left of the font surface
        tx = x - fw / 2
        ty = y + y_offset

        font_surface = font.render(line, True, colour)
        screen.blit(font_surface, (tx, ty))

        y_offset += fh


def run(screen, font, fsize, colors_num):

    def add_score(stage, correct=False) -> None:
        tm = pygame.time.get_ticks()
        if correct:
            GlobalVars.correct_count += 1

            upper_limit = 250
            if tm - GlobalVars.DataCollection[-1][1] != 0:
                scr = round(100000 / (tm - GlobalVars.DataCollection[-1][1]))
                if scr > 666:
                    somevar = True
                elif scr < upper_limit:
                    GlobalVars.score = (scr + GlobalVars.score)
                else:
                    GlobalVars.score = (upper_limit + GlobalVars.score)
            else:
                GlobalVars.score = (upper_limit + GlobalVars.score)
            GlobalVars.DataCollection.append([1, tm, to_enter[stage][0], stage])
            return
        GlobalVars.false_count += 1
        if stage < len(to_enter):
            GlobalVars.DataCollection.append([0, tm, to_enter[stage][0], stage])

    def level1(lst, down_middle=1, down_bottom=1, down_bottom_2=1) -> int:
        #print(lst)
        searched = lst[0]
        answers = lst[1]
        x, y = screen.get_size()
        searched_txt = pygame.font.SysFont(font, fsize * 2).render(searched[0][0], True, searched[1][1])
        text_rect = searched_txt.get_rect(center=(x / 2, y / 2.5 * down_middle))
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
            text_rect = opt_txt.get_rect(center=(x * (it + 1) / 5, y / 1.5 * down_bottom))
            screen.blit(opt_txt, text_rect)

            opt_txt = pygame.font.SysFont(font, fsize * 2).render(labels[it], True, (0, 0, 0))
            text_rect = opt_txt.get_rect(center=(x * (it + 1) / 5, y / 1.2 * down_bottom_2))
            screen.blit(opt_txt, text_rect)
            it += 1

        if corr_answ == -1:
            raise ValueError('No correct answer found')
        return corr_answ

    clock = pygame.time.Clock()
    time_now = 0

    def level2(lst, down_middle=1, down_bottom=1, down_bottom_2=1):
        #print(lst)
        # color is important
        searched = lst[0]
        answers = lst[1]
        x, y = screen.get_size()
        searched_txt = pygame.font.SysFont(font, fsize * 2).render(searched[1][0], True, searched[0][1])
        text_rect = searched_txt.get_rect(center=(x / 2, y / 2.5 * down_middle))
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
            text_rect = pygame.Surface((100, 100)).get_rect(center=(x * (it + 1) / 5, y / 1.5 * down_bottom))
            pygame.draw.rect(screen, opt[0][1], text_rect, width=0)

            opt_txt = pygame.font.SysFont(font, fsize * 2).render(labels[it], True, (0, 0, 0))
            text_rect = opt_txt.get_rect(center=(x * (it + 1) / 5, y / 1.2 * down_bottom_2))
            screen.blit(opt_txt, text_rect)
            it += 1

        if corr_answ == -1:
            raise ValueError('No correct answer found')
        return corr_answ

    def level3(lst, down_middle=1, down_bottom=1, down_bottom_2=1) -> int:
        #print(lst)
        searched = lst[0]
        answers = lst[1]
        x, y = screen.get_size()
        searched_txt = pygame.font.SysFont(font, fsize * 2).render(searched[0][0], True, searched[1][1])
        text_rect = searched_txt.get_rect(center=(x / 2, y / 2.5 * down_middle))
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
            opt_txt = pygame.font.SysFont(font, fsize * 2).render(opt[0][0], True, opt[1][1])
            if opt[0][0] == searched[0][0]:
                corr_answ = it
            text_rect = opt_txt.get_rect(center=(x * (it + 1) / 5, y / 1.5 * down_bottom))
            screen.blit(opt_txt, text_rect)

            opt_txt = pygame.font.SysFont(font, fsize * 2).render(labels[it], True, (0, 0, 0))
            text_rect = opt_txt.get_rect(center=(x * (it + 1) / 5, y / 1.2 * down_bottom_2))
            screen.blit(opt_txt, text_rect)
            it += 1

        if corr_answ == -1:
            raise ValueError('No correct answer found')
        return corr_answ

    def wait(screen, txt_print, args, clock,time_now):

        text = pygame.font.SysFont(font, 18).render("Press ESC to exit", True, (0, 0, 0))
        quit = True
        while quit:
            # Start Page
            screen.fill((255, 255, 255))
            gui(clock, time_now)
            x, y = screen.get_size()
            renderTextCenteredAt(txt_print, pygame.font.SysFont(font, fsize), (0, 0, 0), x / 2, y / 7, screen,
                                 x / 1.5)

            args[0](args[1], args[2],args[3],args[4])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_SPACE:
                        quit = False
                    elif event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            screen.blit(text, (20, 20))
            pygame.display.flip()

    before_iterator = 0

    wait_lst = [['Wybierz nazwę koloru, który został napisany na ekranie.\n W tej sytuacji wybierz V\n \n Naciśnij spację '
                 'aby rozpocząć grę',
                 [
                     level1,
                     [
                         [['zielony', (144, 174, 28)], ['niebieski', (53, 88, 255)]],
                         [
                          [['niebieski', (53, 88, 255)], ['żółty', (254, 175, 22)]],
                          [['żółty', (254, 175, 22)], ['niebieski', (53, 88, 255)]],
                          [['czerwony', (246, 34, 46)], ['zielony', (144, 174, 28)]],
                          [['zielony', (144, 174, 28)], ['czerwony', (246, 34, 46)]]]
                     ],
                     1.2,
                     1,
                     1
                  ]
                 ],

                ['Wybierz kratkę z kolorem, w którym jest napis wyświetlony na ekranie\n W tej sytuacji wybierz V\n Naciśnij spację '
                 'aby rozpocząć grę',
                 [
                     level2,
                     [[['zielony', (144, 174, 28)], ['niebieski', (53, 88, 255)]],
                      [
                          [['niebieski', (53, 88, 255)], ['żółty', (254, 175, 22)]],
                          [['żółty', (254, 175, 22)], ['niebieski', (53, 88, 255)]],
                          [['czerwony', (246, 34, 46)], ['zielony', (144, 174, 28)]],
                          [['zielony', (144, 174, 28)], ['czerwony', (246, 34, 46)]]]],
                     1.1,
                     1,
                     1
                 ]
                 ],
                [
                    'Wybierz nazwę koloru, który został napisany na ekranie.\n W tej sytuacji wybierz X\n \n Naciśnij spację '
                    'aby rozpocząć grę',
                    [
                        level3,
                        [
                            [['żółty', (144, 174, 28)], ['niebieski', (53, 88, 255)]],
                            [
                                [['niebieski', (53, 88, 255)], ['żółty', (254, 175, 22)]],
                                [['żółty', (254, 175, 22)], ['zielony', (144, 174, 28)]],
                                [['czerwony', (246, 34, 46)], ['niebieski', (53, 88, 255)]],
                                [['zielony', (144, 174, 28)], ['czerwony', (246, 34, 46)]]]
                        ],
                        1.2,
                        1,
                        1
                    ]
                    ],
                ]

    def gui(clock, time_now):
        x, y = screen.get_size()
        text = pygame.font.SysFont(font, 18).render("Press ESC to exit", True, (0, 0, 0))
        screen.blit(text, (20, 20))
        mins, txt_s, secs = GlobalVars.ms_to_mins(time_now)
        text = pygame.font.SysFont(font, 25).render(f'{mins}:{txt_s}:{secs}', True, (0, 0, 0))
        screen.blit(text, (x - 150, 20))
        text = pygame.font.SysFont(font, 25).render(f'Wynik: {GlobalVars.score}', True, (0, 0, 0))
        screen.blit(text, (x - 150, 50))
        text = pygame.font.SysFont(font, 25).render(f'Poprawnych opowiedzi: {GlobalVars.correct_count}', True, (0, 0, 0))
        screen.blit(text, (x - 300, 80))
        text = pygame.font.SysFont(font, 25).render(f'Fałszywych opowiedzi: {GlobalVars.false_count}', True, (0, 0, 0))
        screen.blit(text, (x - 300, 110))


    for level in level1, level2, level3:
        wait(screen, wait_lst[before_iterator][0], wait_lst[before_iterator][1],clock, time_now)
        before_iterator += 1
        GlobalVars.DataCollection.append([-1, pygame.time.get_ticks(), -1, -1])
        curr_stage = 0
        stage_1 = GameLogic()
        to_enter = stage_1.game_rounds(color_range=colors_num, rounds=5)
        end_stage = True
        corr_val = 0
        while end_stage:
            clock.tick()
            screen.fill((255, 255, 255))
            x, y = screen.get_size()
            if curr_stage == len(to_enter):
                end_stage = False
                for i in GlobalVars.DataCollection:
                    print(i)
            else:
                corr_val = level(to_enter[curr_stage])

            time_now += clock.get_time()
            gui(clock, time_now)


            # Start Page
            x, y = screen.get_size()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_z:
                        if corr_val == 0:
                            add_score(curr_stage, True)
                            curr_stage += 1
                            break
                        else:
                            add_score(curr_stage)
                            curr_stage += 1
                            break
                    elif event.key == K_x:
                        if corr_val == 1:
                            add_score(curr_stage, True)
                            curr_stage += 1
                            break
                        else:
                            add_score(curr_stage)
                            curr_stage += 1
                            break
                    elif event.key == K_c:
                        if corr_val == 2:
                            add_score(curr_stage, True)
                            curr_stage += 1
                            break
                        else:
                            add_score(curr_stage)
                            curr_stage += 1
                            break
                    elif event.key == K_v:
                        if corr_val == 3:
                            add_score(curr_stage, True)
                            curr_stage += 1
                            break
                        else:
                            add_score(curr_stage)
                            curr_stage += 1
                            break
                    elif event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            pygame.display.flip()

    return time_now