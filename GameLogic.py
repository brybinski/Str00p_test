import numpy as np
from typing import *
import time
import random


class GameLogic:
    colors: list = [
        # primary
        ('niebieski', (53, 88, 255)),
        ('czerwony', (246, 34, 46)),
        ('zielony', (144, 174, 28)),
        # derived
        ('żółty', (254, 175, 22)),
        ('fiolet', (147, 41, 142)),
        ('błękit', (17, 163, 220)),
    ]
    rolled: list
    score: list

    def roll(self, lst=None) -> list:
        if lst is None:
            lst = self.colors

        count: int = len(lst)
        rolled: list[int] = []
        tmp = lst.copy()
        after_roll: list = []

        is_correct = False

        while not is_correct:

            is_correct = True
            after_roll: list = []
            unrolled = tmp.copy()

            for i in range(0, count):
                if len(unrolled) == 1:
                    after_roll.append([tmp[i], unrolled[0]])
                    break

                dice = (random.randint(0, len(unrolled) - 1))
                while dice == i:
                    dice = (random.randint(0, len(unrolled) - 1))

                after_roll.append([tmp[i], unrolled[dice]])
                del unrolled[dice]

            for i in range(0, len(after_roll)):
                if after_roll[i][1] == after_roll[i][0]:
                    is_correct = False

        return after_roll

    def game_rounds(self, color_range=len(colors), rounds=10):
        cols = self.colors[0:color_range]
        while len(cols) < 4:
            for i in cols:
                cols.append(i)

        cols = np.array(cols, dtype=object)
        np.random.shuffle(cols)
        cols = cols.tolist()
        result = []

        for i in range(0, rounds):
            cols = np.array(cols, dtype=object)
            np.random.shuffle(cols)
            cols = cols.tolist()
            rll = self.roll(cols[0:4])

            dice = (random.randint(0, 3))
            if len(result) > 0:
                while rll[dice][0] == result[-1][0][0]:
                    dice = dice + 1
                    dice = dice % 4

            xdice = (random.randint(0, 3))
            while xdice == dice:
                xdice = xdice + 1
                if xdice > 3:
                    xdice = 0

                if len(result) > 0:
                    while rll[xdice][0] == result[-1][0][1]:
                        xdice = xdice + 2
                        xdice = xdice % 4

            result.append([[rll[dice][0], rll[xdice][0]], rll])

        return result

    def __init__(self, colors=None):
        if colors is None:
            self.colors = GameLogic.colors
        else:
            self.colors = GameLogic.colors
        t = int(time.time() * 1000.0)
        random.seed(((t & 0xff000000) >> 24) +
                    ((t & 0x00ff0000) >> 8) +
                    ((t & 0x0000ff00) << 8) +
                    ((t & 0x000000ff) << 24))

        self.score = []


    def __str__(self):
        x = GameLogic()
        res: str = ''
        for i in x.game_rounds(color_range=4):
            res += f'\n{str(i[0])} \n'
            for j in i[1]:
                res+= str(j)+'\n'
        return res